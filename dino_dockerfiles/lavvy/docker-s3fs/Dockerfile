FROM ubuntu:14.04
MAINTAINER Xueshan Feng edited by lavvy <xueshan.feng@gmail.com>

ENV VERSION 1.80
ENV S3User AWSS3User
ENV S3Secret AWSS3Secret
ENV BUCKETNAME mycloudbucketname
ENV MOUNTPOINT /mnt/mountpoint

RUN apt-get update -qq
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
 automake \
 curl \
 build-essential \
 libfuse-dev libcurl4-openssl-dev \
 libtool \
 libxml2-dev mime-support \
 tar \
 && rm -rf /var/lib/apt/lists/*

RUN curl -L https://github.com/s3fs-fuse/s3fs-fuse/archive/v${VERSION}.tar.gz | tar zxv -C /usr/src
RUN cd /usr/src/s3fs-fuse-${VERSION} && ./autogen.sh && ./configure --prefix=/usr && make && make install


ADD s3fs.sh /root/s3fs.sh
RUN chmod +x /root/s3fs.sh

WORKDIR /root

CMD ["/bin/bash"]
