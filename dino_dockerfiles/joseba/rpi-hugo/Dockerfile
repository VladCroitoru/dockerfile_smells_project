FROM resin/raspberrypi3-alpine

LABEL maintainer="joseba.io"

ENV HUGO_VERSION 0.30.2
ENV HUGO_BINARY hugo_${HUGO_VERSION}_Linux-ARM

RUN [ "cross-build-start" ]

RUN apk --update add --no-cache py-pygments bash tar dumb-init

RUN \
  adduser -h /site -s /sbin/nologin -u 1000 -D hugo && \
  apk add --no-cache \
    dumb-init
    
RUN [ "cross-build-end" ]

ADD https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz /usr/bin/
USER    hugo
WORKDIR /site
VOLUME  /site

EXPOSE  1313
ENTRYPOINT ["/usr/bin/dumb-init", "--", "hugo"]
CMD [ "--help" ]
