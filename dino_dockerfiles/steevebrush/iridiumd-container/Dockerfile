# IRD node daemon

FROM appcontainers/ubuntu:xenial
LABEL maintainer="stéphane BROSSE <stevebrush@gmail.com>"

ENV DEBIAN_FRONTEND noninteractive
ENV TIMEZONE Europe/Paris

RUN set -x && \
	buildDeps='build-essential \
		git \
		cmake \
		libboost-system1.58-dev \
		libboost-filesystem1.58-dev \
		libboost-thread1.58-dev \
		libboost-date-time1.58-dev \
		libboost-chrono1.58-dev \
		libboost-regex1.58-dev \
		libboost-serialization1.58-dev \
		libboost-program-options1.58-dev \
		libboost-atomic1.58-dev \
		ca-certificates \
		' && \
	apt-get -qq update -y && \
	apt-get -qq --no-install-recommends install -y $buildDeps && \
	apt-get -qq --no-install-recommends install -y \
		libboost-system1.58.0 \
		libboost-filesystem1.58.0 \
		libboost-thread1.58.0 \
		libboost-date-time1.58.0 \
		libboost-chrono1.58.0 \
		libboost-regex1.58.0 \
		libboost-serialization1.58.0 \
		libboost-program-options1.58.0 \
		libboost-atomic1.58.0 \
		tzdata && \
	echo ${TIMEZONE} > /etc/timezone && \
    ln -fs /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
    dpkg-reconfigure tzdata && \
	git clone https://github.com/iridiumdev/iridium.git /src/iridium && \
	cd /src/iridium && \
 	mkdir build && \
 	cd build && \
 	cmake .. -DCMAKE_CONFIGURATION_TYPES="Release" && \
	make && \
	cp /src/iridium/build/src/connectivity_tool / && \
 	cp /src/iridium/build/src/iridiumd / && \
 	cp /src/iridium/build/src/miner / && \
 	cp /src/iridium/build/src/simplewallet / && \
 	cp /src/iridium/build/src/walletd / && \
 	strip /connectivity_tool && \
 	strip /iridiumd && \
 	strip /miner && \
 	strip /simplewallet && \
 	strip /walletd && \
 	apt-get -qq --auto-remove purge $buildDeps && \
 	apt-get -qq autoclean && \
 	rm -rf /var/lib/apt/lists/* && \
 	rm -rf /src

VOLUME /data

EXPOSE 12007 13007

ENV P2P_BIND_IP 0.0.0.0
ENV P2P_BIND_PORT 12007
ENV P2P_EXTERNAL_PORT 12007
ENV RPC_BIND_IP 127.0.0.1
ENV RPC_BIND_PORT 13007
ENV LOG_FILE /data/iridium.log
ENV LOG_LEVEL 5

ENTRYPOINT ["sh", "-c", "/iridiumd --data-dir /data --log-level $LOG_LEVEL --log-file $LOG_FILE --p2p-bind-ip $P2P_BIND_IP --p2p-bind-port $P2P_BIND_PORT --rpc-bind-ip $RPC_BIND_IP --rpc-bind-port $RPC_BIND_PORT"]
