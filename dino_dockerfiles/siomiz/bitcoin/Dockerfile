FROM ubuntu:trusty

MAINTAINER Tomohisa Kusano <siomiz@gmail.com>

ADD http://keyserver.ubuntu.com:11371/pks/lookup?op=get&search=0xD46F45428842CE5E /tmp/8842ce5e.pub

COPY entrypoint.sh /entrypoint.sh

RUN echo 'deb http://ppa.launchpad.net/bitcoin/bitcoin/ubuntu trusty main' > /etc/apt/sources.list.d/bitcoin.list \
	&& apt-key add /tmp/8842ce5e.pub \
	&& rm /tmp/8842ce5e.pub \
	&& useradd -m bitcoin \
	&& apt-get update \
	&& apt-get install -y bitcoind \
	&& chmod +x /entrypoint.sh

USER bitcoin

VOLUME ["/home/bitcoin"]

WORKDIR /home/bitcoin

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8333

CMD ["/usr/bin/bitcoind"]

