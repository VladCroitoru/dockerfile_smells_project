FROM alpine:3.4
MAINTAINER AJ Bowen <aj@soulshake.net>

ENV HUGO_VERSION=0.18

RUN apk add --update wget ca-certificates python py-pip \
  && wget --no-check-certificate https://github.com/spf13/hugo/releases/download/v0.18/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz \
  && tar xzf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz \
  && rm -r hugo_${HUGO_VERSION}_Linux-64bit.tar.gz \
  && mv hugo_${HUGO_VERSION}_linux_amd64/hugo_${HUGO_VERSION}_linux_amd64 /usr/bin/hugo \
  && rm -r hugo_${HUGO_VERSION}_linux_amd64 \
  && apk del wget ca-certificates \
  && rm /var/cache/apk/*

RUN pip install --upgrade pip && pip install \
    click \
    arrow

COPY ./src /src
WORKDIR /src
EXPOSE 80

ENV HUGO_THEME=blackburn
ENV HUGO_BASEURL=blog.soulshake.net

# build the site
RUN hugo \
    --verbose \
    --log=true \
    --logFile=hugo.log \
    --theme=${HUGO_THEME} \
    --baseUrl=${HUGO_BASEURL} \
    --ignoreCache=true \
    --source=/src \
    --destination=/data/www \
    --config=/src/config.toml


COPY ./make-markdown.py /make-markdown.py
RUN /make-markdown.py /src/content /data/www-md/
