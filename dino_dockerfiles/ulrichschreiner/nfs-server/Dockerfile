FROM alpine:3.4

RUN apk update \
	&& apk add nfs-utils \
	&& rm -rf /var/cache/apk/*

VOLUME /data
EXPOSE 111/udp 2049/tcp
ADD startup.sh /startup.sh
CMD [ "/startup.sh" ]
	
