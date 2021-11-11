FROM debian:buster-20210721-slim

ENV LANG=C.UTF-8

RUN apt-get update -qqy && DEBIAN_FRONTEND=noninteractive apt-get install -qqy --no-install-recommends \
    -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" \
    apt-utils \
    ca-certificates \
    make \
    python3 \
    python3-pip \
    python3-setuptools \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
  && pip3 install --no-cache-dir --disable-pip-version-check \
    "sphinx~=4.1.2" \
    Unidecode \
    "PyYAML~=5.4.1" \
  && rm -rf /root/.cache
COPY legacy_build.sh /usr/local/bin/legacy_build

WORKDIR /compile
VOLUME /compile

CMD ["make"]
