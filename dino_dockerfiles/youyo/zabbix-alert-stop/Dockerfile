FROM golang:1.9-alpine

ENV DIR=/go/src/github.com/youyo/zabbix-alert-stop
ENV PORT=1323
#ENV ZABBIX_USERNAME=
#ENV ZABBIX_PASSWORD=
#ENV ZABBIX_URL=

WORKDIR ${DIR}

ADD *.go ${DIR}/
ADD Gopkg.lock ${DIR}/
ADD Gopkg.toml ${DIR}/
ADD Makefile ${DIR}/

RUN apk add --update --no-cache make git && \
	make setup && \
	make deps

CMD ["make","run"]
