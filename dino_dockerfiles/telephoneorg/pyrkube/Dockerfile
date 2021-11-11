FROM    telephoneorg/debian:stretch

MAINTAINER Joe Black <me@joeblack.nyc>

LABEL   lang.python.version=3
LABEL   app.name=pyrkube

# python3-lxml
RUN     apt-get update && \
            apt-get install -yqq python3 python3-pip && \
            apt-clean --aggressive && \
        pip3 install --upgrade pip requests setuptools six pip

ARG     PYRKUBE_VERSION
ENV     PYRKUBE_VERSION=${PYRKUBE_VERSION:-0.2.5}
LABEL   app.version=$PYRKUBE_VERSION

RUN     pip3 install pyrkube==$PYRKUBE_VERSION

ENV     ENVIRONMENT production
ENV     LOG_LEVEL INFO
ENV     NAMESPACE default
ENV     DOMAIN cluster.local

ENTRYPOINT ["/bin/bash", "-c"]
CMD     ["sleep", "999999"]
