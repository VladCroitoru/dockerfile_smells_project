FROM alpine:3.4
MAINTAINER Volker Machon <volker@machon.biz>

ARG OPTIPNG_VERSION=0.7.6

RUN apk --update add \
           alpine-sdk \
           tar \
           wget \
      && mkdir -p /usr/src/optipng /source \
      && wget -O - http://downloads.sourceforge.net/project/optipng/OptiPNG/optipng-${OPTIPNG_VERSION}/optipng-${OPTIPNG_VERSION}.tar.gz | tar xz -C /usr/src/optipng --strip-components=1 \
      && cd /usr/src/optipng \
      && ./configure \
      && make \
      && make install \
      && rm -rf /usr/src/optipng \
      && apk del alpine-sdk tar wget \
      && rm -rf /var/cache/apk/*

VOLUME ["/source"]
WORKDIR /source
ENTRYPOINT ["/usr/local/bin/optipng"]
CMD ["-quiet", "-strip", "all", "-f4", "-o7", "-preserve", "*.png"]
