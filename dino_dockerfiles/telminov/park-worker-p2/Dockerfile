# docker build -t telminov/park-worker-p2 .
# docker run --rm -ti --name parkworker2 --link parkkeeper --volume=/var/docker/park-worker-p2/conf/:/conf/ telminov/park-worker-p2

FROM ubuntu:14.04
MAINTAINER telminov <telminov@soft-way.biz>

# settings
VOLUME /conf/

RUN apt-get update && \
    apt-get install -y \
                    vim \
                    build-essential \
                    openssh-client \
                    sshpass \
                    python-setuptools \
                    python-dev

RUN easy_install pip

# install
COPY . /opt/park-worker-p2
WORKDIR /opt/park-worker-p2
RUN pip install -e .

WORKDIR /opt/park-worker-p2/parkworker2

ENV ANSIBLE_HOST_KEY_CHECKING=False
CMD test "$(ls /conf/settings.py)" || cp settings.sample.py /conf/settings.py; \
    rm settings.py; \
    ln -s /conf/settings.py settings.py; \
    python bin/start_workers.py
