ARG ALPINE_VERSION
FROM golang:alpine as builder

ENV CGO_ENABLED=0
ENV GOOS=linux
ENV GOPATH=/go
ENV GOBIN=/go/bin

COPY xteve-repo/ /source

WORKDIR /source

RUN apk add --no-cache git 

RUN go get ./... &&\
    go build -o /xteve xteve.go

FROM alpine:${ALPINE_VERSION}

ARG XTEVE_VERSION
ARG XTEVE_COMMIT_REF
ARG DOCKER_XTEVE_COMMIT_REF
ARG BUILD_TIME
ARG BUILD_CI_URL

LABEL org.label-schema.build-date="${BUILD_TIME}" \
    org.label-schema.vcs-ref="${XTEVE_COMMIT_REF}" \
    org.label-schema.vcs-url="https://github.com/xteve-project/xTeVe-Downloads" \
    org.label-schema.version="${XTEVE_VERSION}" \
    org.label-schema.schema-version="1.0" \
    docker-build.vcs-ref="${DOCKER_XTEVE_COMMIT_REF}" \
    docker-build.vcs-url="https://github.com/whi-tw/docker-xteve" \
    docker-build.ci-url="${BUILD_CI_URL}" \
    maintainer="tom@whi.tw"

RUN apk add --no-cache \
    ca-certificates \
    tzdata \
    ffmpeg \
    vlc \
    && update-ca-certificates

WORKDIR /xteve
COPY --from=builder /xteve xteve

VOLUME ["/config", "/tmp/xteve"]

EXPOSE 34400
ENTRYPOINT [ "/xteve/xteve" ]
CMD [ "-config", "/config" ]
