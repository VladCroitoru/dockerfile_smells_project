FROM ubuntu:xenial

# Get needed packages
RUN set -x \
	&& buildDeps=' \
		ca-certificates \
		cmake \
		g++ \
		git \
		libboost-all-dev \
		libssl-dev \
		make \
		pkg-config \
		build-essential \
		libzmq3-dev \
		wget \
		libdb-dev \
		graphviz \
		doxygen \
		curl \
		libtool-bin \
		autoconf \
		automake' \
	&& apt-get -qq update \
	&& apt-get -qq install $buildDeps

# Create app directory
RUN mkdir -p /daemon && mkdir -p /daemon/data && mkdir -p /daemon

# Install Daemon
WORKDIR /daemon/
RUN wget -Lq -O monero-linux-x64.tar.bz2 https://downloads.getmonero.org/cli/monero-linux-x64-v0.14.0.2.tar.bz2
RUN tar -xjf monero-linux-x64.tar.bz2 . && mv -f monero-v*/* .

EXPOSE 18081 18082

WORKDIR /daemon/
