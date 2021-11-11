FROM python:3-alpine3.6

WORKDIR /opt/scaife-cts-api/src/
ENV PATH="/opt/scaife-cts-api/bin:${PATH}" VIRTUAL_ENV="/opt/scaife-cts-api"
COPY requirements.txt ./
RUN set -ex \
    && apk --no-cache add --virtual .build-deps \
      build-base \
      libxml2-dev libxslt-dev \
    && python3 -m venv $VIRTUAL_ENV/ \
    && source $VIRTUAL_ENV/bin/activate \
    && pip install pip wheel -U \
    && pip install -r requirements.txt \
    && apk del .build-deps
COPY logging.ini setup.cfg setup.py ./
COPY scaife_cts_api ./scaife_cts_api
RUN set -ex \
    && runDeps="$( \
      scanelf --needed --nobanner --format '%n#p' --recursive /opt/scaife-cts-api \
        | tr ',' '\n' \
        | sort -u \
        | awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1 }' \
    )" \
    && apk --no-cache add $runDeps \
    && apk --no-cache add --virtual .fetch-deps \
      curl tar \
    && mkdir -p /var/lib/nautilus/data \
    && source $VIRTUAL_ENV/bin/activate \
    && pip --no-cache-dir --disable-pip-version-check install -e . \
    && apk del .fetch-deps
COPY corpus.json ./
ENV ROOT_DIR="/var/lib/nautilus"
RUN scaife-cts-api loadcorpus \
  && scaife-cts-api preload

CMD ["scaife-cts-api", "serve"]
