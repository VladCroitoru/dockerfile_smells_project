FROM alpine:latest

RUN apk add xmlstarlet bash --update --repository http://dl-4.alpinelinux.org/alpine/edge/testing \
	&& rm -rf /var/cache/apk/*

ENTRYPOINT ["xmlstarlet"]
