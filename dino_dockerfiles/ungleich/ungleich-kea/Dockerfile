FROM ubuntu:xenial

MAINTAINER Carlos Ortigoza "carlos.ortigoza@ungleich.ch"

RUN apt-get update \
	&& apt-get install --no-install-recommends -y \
						git \
						g++ \
						automake \
						autoconf \
						libtool \
						pkg-config \
						libboost-all-dev \
						openssl \
						libssl-dev \
						ca-certificates \
						liblog4cplus-dev \
						postgresql-server-dev-all \
						postgresql-client-9.5 \
						libpq-dev \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

RUN cd /root \
	&& git clone https://github.com/isc-projects/kea.git \
	&& cd kea \
	&& git checkout v1_1_0 \
	&& autoreconf --install \
	&& ./configure --with-dhcp-pgsql \
    && make \
    && make install \
    && ldconfig \
    && rm -rf /root/kea

EXPOSE 67/udp

VOLUME /usr/local/etc/kea/

ENTRYPOINT ["kea-dhcp4"]
CMD ["-c", "/usr/local/etc/kea/kea.conf"]
