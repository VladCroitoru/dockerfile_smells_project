FROM ubuntu:16.04
MAINTAINER FBLGIT@GitHub
ENV DEBIAN_FRONTEND=noninteractive
ENV VERSION=v0.4.1
RUN apt-get update && DEBIAN_FRONTEND=noninteractive && apt-get install -qy gcc autoconf make libtool binutils wget
RUN cd /root && wget https://github.com/twitter/twemproxy/archive/${VERSION}.tar.gz && tar zxf ${VERSION}.tar.gz && cd twemproxy-* && \
 autoreconf -fvi && ./configure --prefix=/usr && make -j4 && make install
VOLUME /scripts
COPY start.sh /scripts/start.sh
RUN chmod 755 /scripts/start.sh
CMD ["/scripts/start.sh"]
