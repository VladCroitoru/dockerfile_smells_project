FROM alpine:latest

ENV VERSION 4.0.1
RUN apk --update add \
    autoconf automake bash bison boost-dev boost-program_options \
    boost-serialization build-base curl flex g++ git libstdc++ libtool make \
    mariadb-dev mariadb-libs mysql-client musl postgresql-client postgresql-dev \
    ragel wget
RUN curl -sS https://downloads.powerdns.com/releases/pdns-$VERSION.tar.bz2 | tar xjf - -C . && \
	cd pdns-* && ./configure --with-modules="gpgsql remote" && make && make install && \
	cd .. && rm -fr pdns-*
EXPOSE 53/udp 53/tcp
ENTRYPOINT ["/usr/local/sbin/pdns_server"]
