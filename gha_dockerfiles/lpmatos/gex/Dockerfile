FROM python:3.9.7-alpine3.13

ENV HOME=/home/app/

SHELL ["/bin/sh", "-o", "pipefail", "-c"]
RUN apk add --no-cache bash jpeg-dev zlib-dev tini && \
    adduser -D python && mkdir $HOME && chown -R python:python $HOME

WORKDIR $HOME

COPY [ ".", "gex/" ]

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers && \
    pip install --no-cache-dir -e ./gex && \
    python -m compileall gex/gex && \
    apk del .tmp

USER python

CMD [ "gex" ]
