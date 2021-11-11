# build stage
FROM golang:1.11-alpine as build-env
MAINTAINER mdouchement

RUN apk upgrade
RUN apk add --update --no-cache alpine-sdk git curl

RUN cd /usr/local/bin && \
    curl -SL https://github.com/gobuffalo/packr/releases/download/v1.22.0/packr_1.22.0_linux_amd64.tar.gz | tar xz && \
    chmod +x packr

RUN cd /usr/local/bin && \
    curl -SL https://github.com/goreleaser/goreleaser/releases/download/v0.66.1/goreleaser_Linux_x86_64.tar.gz | tar xz && \
    chmod +x goreleaser

RUN mkdir -p /go/src/github.com/mdouchement/risuto
WORKDIR /go/src/github.com/mdouchement/risuto

ENV CGO_ENABLED 0
ENV GO111MODULE on

COPY . /go/src/github.com/mdouchement/risuto/
# Dependencies
RUN go mod download
# Download static assets
RUN go run risuto.go fetch --min
# Build assets
RUN packr -z
# Packr fix until the filename can be specified/prefix (packr init func must be executed first).
RUN mv web/a_web-packr.go web/assets-packr.go
# Go build
RUN ./build.sh


# final stage
FROM alpine
MAINTAINER mdouchement

ENV ECHO_ENV production
ENV RISUTO_DATABASE /data/tiedot_db

COPY --from=build-env /go/src/github.com/mdouchement/risuto/dist/linux_amd64/risuto /usr/local/bin/

EXPOSE 5000
CMD ["risuto", "server", "-p", "5000"]
