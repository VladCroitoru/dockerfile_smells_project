FROM ubuntu:14.10
MAINTAINER aubrey@hewes.org.uk

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
	apt-get upgrade -y --no-install-recommends && \
	apt-get install -y --no-install-recommends \
		build-essential \
		libssl-dev \
		ncurses-dev \
		wget

# @todo use script to dynamically define and retrieve latest version
# @see https://gist.github.com/AubreyHewes/261748ad940a0be64f28
ENV VERSION 1.2.1
RUN wget "http://downloads.sourceforge.net/project/bitchx/ircii-pana/bitchx-${VERSION}/bitchx-${VERSION}.tar.gz" && \
	tar -xzf bitchx-${VERSION}.tar.gz && \
	cd bitchx-${VERSION} && \
	./configure --prefix=/usr --with-ssl --with-plugins --enable-ipv6 && \
	make && \
	make install && \
	rm -rf /bitchx-*

ENTRYPOINT ["/usr/bin/BitchX"]
#
# TO RUN: docker run -u $(id -u) -v ${HOME}/.BitchX:/root/.BitchX -it bitchx -n ${USER} $@
#
