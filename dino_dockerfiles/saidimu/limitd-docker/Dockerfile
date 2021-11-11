FROM node:0.10

# Dockerfile author/maintainer
MAINTAINER Saidimu Apale (saidimu@gmail.com)

## limitd releases: https://github.com/auth0/limitd/releases
ENV LIMITD_VERSION v4.1.2
# ENV LIMITD_URL https://codeload.github.com/auth0/limitd/tar.gz/${LIMITD_VERSION}
ENV LIMITD_URL https://github.com/auth0/limitd/archive/${LIMITD_VERSION}.tar.gz
ENV LIMITD_HOME /src/
RUN mkdir -p ${LIMITD_HOME} \
    && mkdir -p /data
WORKDIR ${LIMITD_HOME}

RUN curl -SL ${LIMITD_URL} -o limitd.tar.gz \
    && tar -xf limitd.tar.gz --strip-components=1 \
    && npm install \
    && rm limitd.tar.gz

COPY ./limitd.yml ${LIMITD_HOME}

VOLUME /data

EXPOSE 9001

CMD ./bin/limitd --config-file limitd.yml
