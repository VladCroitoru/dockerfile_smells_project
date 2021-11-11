FROM golang:1.10-alpine as build

WORKDIR /go/src/githib.com/marcinbudny/ravendb_exporter
COPY . ./
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -tags netgo -ldflags '-extldflags "-static"' -o app

FROM busybox:1.28
COPY --from=build /go/src/githib.com/marcinbudny/ravendb_exporter/app /
VOLUME /certs
EXPOSE 9440
ENTRYPOINT [ "/app" ]
