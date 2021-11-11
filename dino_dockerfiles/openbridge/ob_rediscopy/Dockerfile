##
##  Redis Back Up
##  Last revised 02/09/2017
##

FROM alpine:edge
MAINTAINER Thomas Spicer (thomas@openbridge.com)

ENV LANG C.UTF-8

ENV PY_DEPS \
      curl \
      python \
      python-dev \
      git
RUN echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
    && apk update \
    && apk add --update --no-cache --virtual .build-deps \
       $PY_DEPS \
    && curl -fSL 'https://bootstrap.pypa.io/get-pip.py' | python \
    && pip install --no-cache-dir redis ijson nose awscli -U \
    && find /usr/local -depth \
        \( \
            \( -type d -a -name test -o -name tests \) \
            -o \
            \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        \) -exec rm -rf '{}' + \
    && apk add --update --virtual .python-deps \
        python \
        bash \
        curl \
    && cd /usr/local/bin/ \
    && git clone https://github.com/p/redis-dump-load.git \
    && cd redis-* \
    && python setup.py install \
    && ln /usr/local/bin/redis-dump-load/redisdl.py redis-tool \
    && rm -rf /usr/src/python ~/.cache \
    && rm -Rf /tmp/* \
    && apk del .build-deps

COPY docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD [""]
