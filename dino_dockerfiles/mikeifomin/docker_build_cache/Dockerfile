FROM ubuntu:16.04

WORKDIR /root

RUN apt-get update && apt-get install -y --no-install-recommends \
   ca-certificates \ 
   git \
   gcc \
   make \
   automake \
   autoconf \
   libtool \
   libltdl-dev \
   build-essential libssl-dev \
   devscripts \
   openssl 

RUN git clone https://github.com/squid-cache/squid.git
WORKDIR /root/squid
RUN git checkout v4.0
RUN autoreconf --install
RUN autoconf
RUN ./configure \
    --prefix= \
    --with-openssl \
    --enable-ssl-crtd

RUN make && make install

CMD ["/sbin/squid", "-X"]


