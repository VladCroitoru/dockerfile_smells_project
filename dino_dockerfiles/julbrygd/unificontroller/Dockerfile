FROM alpine as build
ENV UNIFI_VERSION=5.12.35

RUN apk -U add --no-cache -t build-deps binutils curl && \
	mkdir /data && \
	cd /data && \
	curl -OL https://dl.ubnt.com/unifi/${UNIFI_VERSION}/UniFi.unix.zip && \
	curl -OL https://dl.ubnt.com/unifi/${UNIFI_VERSION}/unifi_sh_api && \
	unzip UniFi.unix.zip && \
	mv unifi_sh_api UniFi/bin/ && \
	apk --no-cache del build-deps 
	

FROM frolvlad/alpine-java:jdk8-full
LABEL maintainer="Stephan Conrad <stephan@conrad.pics>"

ENV UNIFI_MONGO_DB_HOST="mongo" \
	UNIFI_MONGO_DB_USE_AUTH="FALSE" \
	UNIFI_MONGO_DB_USER="" \
	UNIFI_MONGO_DB_PASS="" \
	UNIFI_MONGO_DB_NAME="ace" \
	UNIFI_MONGO_DB_STAT_NAME="ace-stat" \
	UNIFI_MONGO_DB_PORT="27017" \
	UNIFI_MONGO_DB_WAIT_TIMEOUT="60"

COPY --from=build /data/UniFi /srv/unifi
COPY root/ /
RUN apk -U add --no-cache libstdc++ && \
	mkdir /var/lib/unifi && \
	ln -s /var/lib/unifi /srv/unifi/data && \
	mkdir /var/log/unifi && \
	ln -s /var/log/unifi /srv/unifi/logs && \
	ln -s /dev/stdout /srv/unifi/logs/server.log && \
	mkdir /var/run/unifi && \
	ln -s /var/run/unifi /srv/unifi/run

EXPOSE 3478/udp 6789/tcp 8080/tcp 8443/tcp 8843/tcp 8880/tcp 8881/tcp 8882/tcp
VOLUME /var/lib/unifi

ENTRYPOINT ["/usr/bin/entrypoint.sh"]
CMD ["unifi_controller_start"]
