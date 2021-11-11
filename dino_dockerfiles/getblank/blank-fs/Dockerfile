FROM getblank/busybox
MAINTAINER Opryshko Alexandr <sclif13@gmail.com>

RUN wget http://releases.getblank.net/blank-fs/linux/blank-fs -O /bin/blank-fs \
&& chmod +x /bin/blank-fs \
&& mkdir /app

WORKDIR /app
EXPOSE 8082
CMD blank-fs -s ws://blank-sr:1234
