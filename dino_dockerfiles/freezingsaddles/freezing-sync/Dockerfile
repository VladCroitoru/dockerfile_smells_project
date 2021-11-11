# BUILD
# =====

FROM ubuntu:xenial as buildstep
LABEL maintainer="Richard Bullington-McGuire <richard@obscure.org>"

COPY resources/docker/sources.list /etc/apt/sources.list
RUN apt-get update

RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update

RUN apt-get install -y python3.6 python3.6-dev curl build-essential git

RUN mkdir -p /build/wheels
RUN curl https://bootstrap.pypa.io/get-pip.py | python3.6

RUN pip3 install --upgrade pip setuptools wheel

ADD requirements.txt /tmp/requirements.txt
RUN pip3 wheel -r /tmp/requirements.txt --wheel-dir=/build/wheels

# Now build the wheel for this project too.
ADD . /app
WORKDIR /app

RUN python3.6 setup.py bdist_wheel -d /build/wheels


# DEPLOY
# =====

FROM ubuntu:xenial as deploystep
LABEL maintainer="Richard Bullington-McGuire <richard@obscure.org>"

COPY resources/docker/sources.list /etc/apt/sources.list

RUN apt-get update \
  && apt-get install -y software-properties-common curl \
  && add-apt-repository -y ppa:deadsnakes/ppa \
  && apt-get update \
  && apt-get install -y python3.6 --no-install-recommends \
  && apt-get clean \
  && curl https://bootstrap.pypa.io/get-pip.py | python3.6 \
  && pip3 install --upgrade pip setuptools wheel \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /data/cache/activities
RUN mkdir -p /data/cache/weather

VOLUME /data

COPY --from=buildstep /build/wheels /tmp/wheels

RUN pip3 install /tmp/wheels/*

CMD freezing-sync
