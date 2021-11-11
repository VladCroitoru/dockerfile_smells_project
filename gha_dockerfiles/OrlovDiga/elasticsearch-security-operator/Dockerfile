# Build the manager binary
FROM golang:1.16.3-alpine3.13 as build
ARG ARTIFACT_VERSION
WORKDIR /go/src/elasticsearch-security-operator/
COPY . .

ENV CGO_ENABLED=0 \
    GO111MODULE=on \
    GOFLAGS=""

RUN go mod download
RUN go install \
    -installsuffix "static" \
    -ldflags "                                            \
        -X main.Version=${ARTIFACT_VERSION}               \
        -X main.GoVersion=$(go version | cut -d " " -f 3) \
        -X main.Platform=$(go env GOOS)/$(go env GOARCH)  \
    " \
    ./...

FROM alpine:3.13.5 as runtime
RUN set -x \
    && apk add --update --no-cache ca-certificates tzdata \
    && update-ca-certificates \
    && echo 'Etc/UTC' > /etc/timezone \
    adduser -S appuser -u 1000
ENV TZ     :/etc/localtime
ENV LANG   en_US.utf8
ENV LC_ALL en_US.UTF-8
COPY --from=build /go/bin/elasticsearch-security-operator /elasticsearch-security-operator
USER 1000
ENTRYPOINT ["/elasticsearch-security-operator"]
