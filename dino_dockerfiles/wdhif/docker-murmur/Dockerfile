FROM ubuntu
LABEL maintainer "Wassim DHIF <wassimdhif@gmail.com>"

RUN \
	apt-get update -y && \
	apt-get install -y mumble-server && \
	/etc/init.d/mumble-server stop && \
	touch /murmur.sqlite

COPY murmur-config.ini /murmur-config.ini
COPY start-murmur.sh /start-murmur.sh

EXPOSE 64738/tcp 64738/udp

ENTRYPOINT ["/start-murmur.sh"]
