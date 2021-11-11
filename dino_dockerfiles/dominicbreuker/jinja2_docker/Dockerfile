FROM alpine:3.5

ENV GOSU_VERSION 1.7

RUN apk update && \
  apk add --no-cache --update-cache curl bash && \
  curl -o /usr/local/bin/gosu -L https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64  && \
  chmod +x /usr/local/bin/gosu && \
  rm -rf /var/cache/apk/* /usr/local/src/*

ENV PUID 1000
ENV PGID 1000

RUN apk add --update \
  python-dev \
  python \
  sshpass \
  sudo \
  py-pip && \
  pip install --upgrade pip && \
  pip install \
  PyYAML \
  Jinja2 \
  httplib2 \
  urllib3 \
  simplejson

## Cleanup
RUN apk del \
  python-dev \
  make && \
  rm -rf /var/cache/apk/*

# create dev user
RUN addgroup -g $PGID dev && \
  adduser -h /config -u $PUID -H -D -G dev -s /bin/bash dev && \
  mkdir -p /home/dev/bin && \
  sed -ri 's/(wheel:x:10:root)/\1,dev/' /etc/group && \
  sed -ri 's/# %wheel ALL=\(ALL\) NOPASSWD: ALL/%wheel ALL=\(ALL\) NOPASSWD: ALL/' /etc/sudoers

# Create a shared data volume
# We need to create an empty file, otherwise the volume will
# belong to root.
RUN mkdir /data/ /out/ && \
 touch /data/.extra /out/.extra && \
 chown -R dev:dev /data && \
 chown -R dev:dev /out

## Expose some volumes
VOLUME ["/data", "/out"]

ENV TEMPLATES_DIR /data
ENV OUT_DIR /out
ENV TEMPLATE my.tmpl

COPY render.py /home/dev/bin/render.py
RUN chown -R dev:dev /home/dev && chmod 700 /home/dev/bin/render.py

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
WORKDIR /data

ENTRYPOINT ["docker-entrypoint.sh"]
