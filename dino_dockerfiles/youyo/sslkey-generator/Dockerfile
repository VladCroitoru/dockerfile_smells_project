FROM golang:1.9-alpine
LABEL maintainer "youyo <1003ni2@gmail.com>"

ENV DIR /go/src/github.com/youyo/sslkey-generator/
ENV PORT 1323

WORKDIR ${DIR}

ADD . ${DIR}
RUN apk add --update --no-cache --virtual _dependencies git && \
	apk add --no-cache make && \
	make setup && \
	make deps && \
	apk del _dependencies

EXPOSE ${PORT}:${PORT}
CMD ["make", "run"]
