FROM alpine
MAINTAINER Félix Saparelli <me@passcod.name>

CMD /start.sh
ENV S3_BASEURL https://s3.amazonaws.com
EXPOSE 80

RUN apk add --update --no-cache \
      autoconf automake build-base caddy \
      curl-dev fuse fuse-dev git libcurl \
      libgcc libssh2 libstdc++ libxml2 \
      libxml2-dev openssl openssl-dev &&\
    git clone --depth=1 git://github.com/s3fs-fuse/s3fs-fuse.git &&\
    cd s3fs-fuse && ./autogen.sh && ./configure &&\
    make && make install && cd .. && rm -rf s3fs-fuse &&\
    apk del --purge \
      autoconf automake build-base curl-dev \
      fuse-dev git libxml2-dev openssl-dev

COPY start.sh /
