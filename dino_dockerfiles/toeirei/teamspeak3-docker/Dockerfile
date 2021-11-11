FROM alpine:latest

LABEL   maintainer "Viktoria Rei Bauer"

ENV	TS_USER=teamspeak \
	TS_HOME=/teamspeak


RUN	set -x \
    	&& apk update \
    	&& apk --no-cache add ca-certificates wget openssl bash \
    	&& update-ca-certificates \
    	&& apk --no-cache --virtual add w3m bzip2

		
# Get us a glibc
RUN wget --no-check-certificate https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk -O /tmp/glibc-2.30-r0.apk
RUN apk add --allow-untrusted /tmp/glibc-2.30-r0.apk && rm /tmp/glibc-2.30-r0.apk
		
RUN     addgroup -S \
		-g 911 \
           	${TS_USER} \
        && adduser -S \
            	-u 911 \
            	-G ${TS_USER} \
            	-D \
		$TS_USER

WORKDIR	${TS_HOME}


# Get teamspeak package
RUN	TS_SERVER_VER="$(w3m -dump https://www.teamspeak.com/downloads | grep -m 1 'Server 64-bit ' | awk '{print $NF}')" \
	&& wget http://files.teamspeak-services.com/releases/server/${TS_SERVER_VER}/teamspeak3-server_linux_amd64-${TS_SERVER_VER}.tar.bz2 -O /tmp/teamspeak.tar.bz2 \
  	&& tar jxf /tmp/teamspeak.tar.bz2 -C /tmp \
  	&& mv /tmp/teamspeak3-server_*/* ${TS_HOME}

# Clean up
RUN	set -x \
    	&& rm /tmp/teamspeak.tar.bz2 \
    	&& rm -rf /tmp/*

RUN 	cp "$(pwd)/redist/libmariadb.so.2" $(pwd)

ADD 	entrypoint.sh ${TS_HOME}/entrypoint.sh

RUN 	chown -R ${TS_USER}:${TS_USER} ${TS_HOME} && chmod +x entrypoint.sh

USER  	${TS_USER}

EXPOSE 	9987/udp
EXPOSE 	10011
EXPOSE 	30033

ENTRYPOINT ["/teamspeak/entrypoint.sh"]
