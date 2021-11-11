FROM hivesolutions/ubuntu:rolling

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

VOLUME /mnt/builds

ADD . /builder

WORKDIR /build

RUN rm -rf /builder/.git
RUN apt-get update && apt-get install -y -q make
RUN cd /builder && make install

CMD ["/builder/build.sh"]
