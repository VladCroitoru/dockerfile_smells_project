FROM mercadolibre/melibuntu:latest
MAINTAINER Arquitectura <arquitectura@mercadolibre.com>

USER root

ENV PYTHON_VERSION=2.7.11

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    python2.7 \
    python2.7-dev \
    python2.7-doc \
    && rm -rf /var/lib/apt/lists/*

RUN set -xe \
    && curl -k -SL https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python2.7 get-pip.py \
    && pip install virtualenv

RUN mkdir -p /commands
COPY ./commands/*.sh /commands/

ONBUILD ADD ./ /app/
ONBUILD WORKDIR /app
ONBUILD CMD /commands/test.sh && /commands/package.sh
ONBUILD RUN /commands/run.sh
