FROM alpine:latest

LABEL maintainer="Miguel Terron <miguel.a.terron@gmail.com>"

ARG BUILD_DATE
ARG VCS_REF
ARG RETHINKDB_VERSION=2.3.6

LABEL org.label-schema.build-date=$BUILD_DATE \
	org.label-schema.vcs-url="https://github.com/mterron/rethinkdb.git" \
	org.label-schema.vcs-ref=$VCS_REF \
	org.label-schema.schema-version="1.0.0-rc.1" \
	org.label-schema.version=$RETHINKDB_VERSION \
	org.label-schema.description="Alpine based RethinkDB image"

RUN echo "Rethinkdb for Alpine Linux" &&\
	apk --no-cache upgrade &&\
	apk --no-cache add rethinkdb su-exec &&\
	mkdir /data &&\
	chown daemon:daemon /data &&\
	apk --no-cache info -v | sed "s/-r\d*$//g"|sed 's/\(.*\)-/\1 /' > /etc/manifest.txt

VOLUME ["/data"]

WORKDIR /data

ENTRYPOINT RETHINKDB_CLUSTER_IP_ADDR=${RETHINKDB_CLUSTER_IP_ADDR:=$(nslookup ${RETHINKDB_SVC_NAME:=rethinkdb} 127.0.0.1 2>/dev/nul|awk '{print $3}'|egrep -v "(127.0.0.1|^$|$(hostname -i))"|sort|head -1)} exec su-exec daemon:daemon rethinkdb --bind all -d /data -n ${HOSTNAME} --server-tag ${RETHINKDB_TAGS:=default} --join "${RETHINKDB_CLUSTER_IP_ADDR:=localhost}:${RETHINKDB_CLUSTER_PORT:=29015}" --join-delay $((RANDOM%50+9)) --cluster-reconnect-timeout 600 --no-update-check 


#Ports:	process cluster webui
EXPOSE	28015 	29015 	8080
