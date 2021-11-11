FROM python:2.7-alpine
MAINTAINER Mike Dougherty <mike.dougherty@gmail.com>

WORKDIR /src
VOLUME /output
ENV LC_ALL=C
ENV OUTPUT_DIR /output
ENV OUTPUT_FORMAT dot
ENTRYPOINT ["/src/entrypoint.sh"]

RUN apk add --update \
        graphviz \
        libxslt \
        libxml2 \
    && apk del --purge \
    && rm /var/cache/apk/*

COPY requirements.txt /src
RUN buildDeps='\
        libxml2-dev \
        libxslt-dev \
        gcc \
        python-dev \
        build-base' \
    && apk add --update $buildDeps\
    && pip install -r requirements.txt \
    && apk del --purge $buildDeps \
    && rm /var/cache/apk/*

COPY . /src
