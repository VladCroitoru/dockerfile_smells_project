FROM ubuntu:xenial

RUN set -ex \
&& apt-get update \
    && apt-get install -qyy \
      -o APT::Install-Recommends=false -o APT::Install-Suggests=false \
    python-pip python-setuptools \
    && rm -rf /var/lib/apt/lists/* \
    && pip install awscli

ENTRYPOINT ["/usr/local/bin/aws"]

CMD ["--help"]
