FROM python:3.6.4-alpine3.7

MAINTAINER Steve McQuaid <steve@stevemcquaid.com>

ENV VERSION 0.0.2

RUN apk add --update \
    py-pip \
    build-base; \
    rm -rf /var/cache/apk/*

RUN pip install --upgrade pip


# Deps for matplotlib
RUN apk add --update \
    freetype-dev \
    libjpeg-turbo-dev \
    libpng-dev \
    make \
    automake \
    gcc \
    g++ \
    subversion \
    python3-dev; \
    rm -rf /var/cache/apk/*

WORKDIR /src

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . /src

CMD ["python"]

