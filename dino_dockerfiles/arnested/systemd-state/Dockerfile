FROM golang:1.17.3-alpine AS build-env

WORKDIR /build

ENV GO111MODULE=on
ENV CGO_ENABLED=0
ENV GOOS=linux

RUN apk --no-cache add git=~2 upx=~3

COPY *.go go.mod go.sum /build/

RUN go version
RUN go build -tags docker -ldflags '-s -w'
RUN go test -o ./systemd-state.test -v -cover -ldflags '-s -w'
RUN upx systemd-state systemd-state.test

FROM scratch

EXPOSE 80

ENV PATH=/

COPY --from=build-env /build/systemd-state /systemd-state
COPY --from=build-env /build/systemd-state.test /test

HEALTHCHECK CMD ["/systemd-state", "-healthcheck"]

ENTRYPOINT ["systemd-state"]

LABEL \
        org.opencontainers.image.title="systemd state http server" \
        org.opencontainers.image.description="A small HTTP server exposing the overall state of systemd" \
        org.opencontainers.image.licenses="MIT" \
        org.opencontainers.image.authors="Arne Jørgensen <arne@arnested.dk>"
