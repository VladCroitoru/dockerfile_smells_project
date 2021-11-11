FROM docker
MAINTAINER zbyte64@gmail.com

ENV S3FS_VERSION "1.80"

RUN apk --update add fuse alpine-sdk automake autoconf libxml2-dev fuse-dev curl-dev git bash wget
ADD https://github.com/s3fs-fuse/s3fs-fuse/archive/v${S3FS_VERSION}.tar.gz /tmp/s3fs-fuse.tar.gz

ADD ./build.sh /usr/local/bin/build.sh
RUN chmod +x /usr/local/bin/build.sh

WORKDIR /tmp

RUN tar xvzf /tmp/s3fs-fuse.tar.gz
WORKDIR /tmp/s3fs-fuse-${S3FS_VERSION}
RUN ./autogen.sh
RUN ./configure --prefix=/usr
RUN make
RUN make install

RUN mkdir -p /var/source-code/.git
VOLUME /var/source-code

CMD ["build.sh"]
