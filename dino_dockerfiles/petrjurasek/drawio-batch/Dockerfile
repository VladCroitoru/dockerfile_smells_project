FROM python:3.6.4-slim-stretch
MAINTAINER Petr Jurasek

ENV DRAWIOBATCH_VERSION 8.2.2
ENV PHANTOMJS_VERSION 2.1.1

RUN apt-get update && apt-get install -y wget bzip2 libfontconfig1 && \
    cd /tmp && \
    wget https://github.com/languitar/drawio-batch/archive/${DRAWIOBATCH_VERSION}.tar.gz && \
    tar xfvz ${DRAWIOBATCH_VERSION}.tar.gz && \
    cd drawio-batch-${DRAWIOBATCH_VERSION} && \
    python3 setup.py install && \
    cd /tmp && \
    wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2 && \
    tar xfvj phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2 && \
    mv phantomjs-${PHANTOMJS_VERSION}-linux-x86_64/bin/phantomjs /usr/bin/phantomjs && \
    chmod +x /usr/bin/phantomjs && \
    rm -rf /tmp/* && \
    mkdir /.cache && \
    chmod 777 /.cache

RUN mkdir /code
WORKDIR /code 

COPY docker-entrypoint.sh /usr/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]
