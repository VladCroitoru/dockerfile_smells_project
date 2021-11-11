FROM alpine:latest
MAINTAINER Gepser Hoil <gepser@luna.com.gt>

ENV HUGO_VERSION=0.19
RUN apk add --update wget ca-certificates && \
  cd /tmp/ && \
  wget https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \
  tar xzf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \
  rm -r hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \
  mv hugo*/hugo* /usr/bin/hugo && \
  apk del wget ca-certificates && \
  rm /var/cache/apk/*
  
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

VOLUME ["/src", "/destination"]

WORKDIR /src
CMD ["/entrypoint.sh"]

EXPOSE 1313
