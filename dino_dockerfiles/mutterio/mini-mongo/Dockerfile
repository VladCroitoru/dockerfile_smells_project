FROM alpine:edge

RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" \
			>> /etc/apk/repositories && \
    apk upgrade --update && \
    apk add mongodb@testing  &&\
		rm -rf /var/cache/apk/*

ADD dosu /sbin/
RUN chmod +x /sbin/dosu

ADD entrypoint.sh /entrypoint.sh
EXPOSE 27017
VOLUME /data

ENTRYPOINT ["/entrypoint.sh"]
CMD ["mongod","--bind_ip","0.0.0.0","--dbpath","/data","--nounixsocket","--journal","--cpu","--noprealloc"]
