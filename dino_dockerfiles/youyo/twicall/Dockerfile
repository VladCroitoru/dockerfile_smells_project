FROM golang:1-alpine
LABEL maintainer "youyo <1003ni2@gmail.com>"

ENV DIR=/go/src/github.com/youyo/twicall
WORKDIR ${DIR}
ADD . ${DIR}/
RUN apk add --update --no-cache git make && \
	make setup && \
	make deps
CMD ["make","run"]
