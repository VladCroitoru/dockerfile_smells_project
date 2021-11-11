FROM alpine:edge
MAINTAINER George Kutsurua <g.kutsurua@gmail.com>

RUN apk --no-cache add redis &&\
	rm -rf /var/cache/apk/*

EXPOSE 6379

ENTRYPOINT ["/usr/bin/redis-server"]
CMD ["--port", "6379"]
