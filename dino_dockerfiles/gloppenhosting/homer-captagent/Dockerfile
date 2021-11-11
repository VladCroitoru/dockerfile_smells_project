FROM debian:jessie
MAINTAINER Andreas Krüger
ENV DEBIAN_FRONTEND noninteractive
ENV captagent_version 0x00001

RUN apt-get update -qq && apt-get install --no-install-recommends --no-install-suggests -yqq ca-certificates git make m4 automake autoconf libtool libcap-dev libexpat-dev libpcap-dev zlib1g-dev openssl libssl-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src
RUN git clone --depth 1 https://github.com/sipcapture/captagent.git .

WORKDIR /usr/src/captagent
RUN ./build.sh
RUN ./configure --enable-ssl --enable-compression
RUN make && make install

WORKDIR /
COPY captagent.xml /usr/local/etc/captagent/captagent.xml
COPY run.sh /

EXPOSE 8909
ENTRYPOINT [ "/run.sh" ]
