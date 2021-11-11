FROM golang:1.10-alpine as BUILD

RUN apk update && apk upgrade
RUN apk add make gcc git musl-dev

COPY ./ /go/src/github.com/Axway/elasticsearch-docker-beat
WORKDIR /go/src/github.com/Axway/elasticsearch-docker-beat

ARG LDFLAGS="-s -w"
RUN make LDFLAGS="${LDFLAGS}"
RUN go build -ldflags "${LDFLAGS}" -o ./updater /go/src/github.com/Axway/elasticsearch-docker-beat/starter/main.go

FROM alpine:3.8

RUN apk --no-cache add curl
COPY --from=BUILD /go/src/github.com/Axway/elasticsearch-docker-beat/elasticsearch-docker-beat /etc/dbeat/dbeat
COPY --from=BUILD /go/src/github.com/Axway/elasticsearch-docker-beat/updater /etc/dbeat/updater
COPY ./start.sh /etc/dbeat/start.sh
COPY ./dbeat-confimage.yml /etc/beatconf/dbeat.yml
COPY ./*.json /etc/dbeat/

WORKDIR /etc/dbeat

HEALTHCHECK --interval=10s --timeout=15s --retries=12 CMD curl -s -f localhost:3000/api/v1/health

ENTRYPOINT [ "/etc/dbeat/start.sh" ]
CMD [ "-c", "/etc/beatconf/dbeat.yml" ]

# For remote debugging purposes
# CMD ["/usr/local/bin/dlv", "--listen=:2345", "--headless=true", "--api-version=2", "exec", "/etc/dbeat/dbeat", "--", "-e", "-c", "/etc/beatconf/dbeat.yml", "-strict.perms=false"]
