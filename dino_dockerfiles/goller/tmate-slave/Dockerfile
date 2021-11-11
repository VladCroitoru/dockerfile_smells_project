FROM gliderlabs/alpine:latest
MAINTAINER Chris Goller <goller@gmail.com>

ADD . /src
ADD run.sh create_keys.sh /usr/local/bin/
	
RUN 	apk update && \
	apk add ncurses libevent openssh ncurses-terminfo && \
	apk add git automake autoconf libtool pkgconf build-base zlib-dev openssl-dev libevent-dev ncurses-dev cmake ruby && \
	cd src && \
	mkdir -p etc && \
	aclocal && \
	automake --add-missing --force-missing --copy --foreign && \
	autoreconf && \
	./configure && \
	make && \
	make install && \
	apk del git automake autoconf libtool pkgconf build-base zlib-dev openssl-dev libevent-dev ncurses-dev cmake ruby && \
	cd .. && \
	rm -rf /src 

CMD ["/usr/local/bin/run.sh"]
