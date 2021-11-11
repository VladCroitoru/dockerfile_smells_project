FROM alpine:3.3

RUN set -ex \
  && mkdir -p /usr/src \
  && apk add --no-cache --virtual .fetch-deps curl \
  && curl 'http://www.eblong.com/zarf/glk/cheapglk-104.tar.gz' -o /usr/src/cheapglk.tar.gz \
  && curl 'http://www.eblong.com/zarf/glulx/glulxe-052.tar.gz' -o /usr/src/glulxe.tar.gz \
  && tar -zxvf /usr/src/cheapglk.tar.gz -C /usr/src \
  && tar -zxvf /usr/src/glulxe.tar.gz -C /usr/src \
  && apk add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    make \
  && cd /usr/src/cheapglk \
  && make \
  && cd /usr/src/glulxe \
  && make \
  && mv /usr/src/glulxe/glulxe /usr/local/bin/glulxe \
  && apk del .fetch-deps \
  && apk del .build-deps \
  && rm -rf /usr/src

COPY Pancakes.materials/Release/Pancakes.gblorb /

CMD ["/usr/local/bin/glulxe", "/Pancakes.gblorb"]
