FROM ubuntu:xenial
MAINTAINER Lewis Lambert <lewis.lambert@zserve.co.uk>

ENV TERM xterm
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
	&& apt-get upgrade -q -y \
	&& apt-get install -q -y wget vim python sqlite3 libsqlite3-dev python-dev python-pip git \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& cd /tmp \
	&& wget https://www.multichain.com/download/multichain-1.0.4.tar.gz \
	&& tar -xvzf multichain-1.0.4.tar.gz \
	&& cd multichain-1.0.4 \
	&& mv multichaind multichain-cli multichain-util /usr/local/bin \
	&& cd /tmp \
	&& rm -Rf multichain*

RUN cd / \
	&& pip install pycrypto \
	&& git clone https://github.com/MultiChain/multichain-explorer.git

VOLUME [ "/opt/chains" ]

EXPOSE 8333 8332 18333 18332
