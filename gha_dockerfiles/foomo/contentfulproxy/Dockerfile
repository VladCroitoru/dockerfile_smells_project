##############################
###### STAGE: BUILD     ######
##############################
FROM golang:1.17-alpine AS build-env

ENV GO111MODULE=on

RUN apk add --no-cache upx

WORKDIR /src

COPY go.mod go.sum ./

RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    go mod download

COPY ./ ./

RUN GOARCH=amd64 GOOS=linux CGO_ENABLED=0  go build -ldflags "-w -s" -trimpath -o ./bin/contentfulproxy cmd/contentfulproxy/main.go

ENV UPX="-1"
RUN upx /src/bin/contentfulproxy

##############################
###### STAGE: PACKAGE   ######
##############################
FROM alpine:latest

ENV CONTENTFULPROXY_SERVER_ADDR=0.0.0.0:80
ENV LOG_JSON=1

RUN apk add --update --no-cache ca-certificates

COPY --from=build-env /src/bin/contentfulproxy /usr/sbin/contentfulproxy

EXPOSE 80
# Zap
EXPOSE 9100
# Prometheus
EXPOSE 9200
# Viper
EXPOSE 9300

ENTRYPOINT ["/usr/sbin/contentfulproxy"]

CMD ["-webserver-address=$CONTENTFULPROXY_SERVER_ADDR"]
