FROM python:3-alpine
MAINTAINER Hendrik Spohr <hendrik.spohr@gmx.net>

RUN set -e \
  && apk add --no-cache --virtual .build-deps git \
  && pip install git+https://github.com/sivel/speedtest-cli.git \
  && apk del .build-deps \
  && rm -fr /root/.cache /lib/apk

ENTRYPOINT [ "speedtest-cli" ]
