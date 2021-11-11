FROM golang:1.9 as builder

ARG DRONE_CLI_VERSION=v0.8.5
ARG DRONE_CLI_REPO=github.com/drone/drone-cli
ARG DRONE_CLI_PACKAGE=$DRONE_CLI_REPO/drone

RUN set -x \
 && go get -v -d "$DRONE_CLI_PACKAGE" \
 && cd "$GOPATH/src/$DRONE_CLI_REPO" \
 && git checkout --detach \
 && git reset --hard "$DRONE_CLI_VERSION" \
 && git clean -df \
 && CGO_ENABLED=0 go build -a \
      -ldflags "-X main.version=${DRONE_CLI_VERSION##v} -s -extldflags '-static'" \
      -o /usr/local/bin/drone \
      "$DRONE_CLI_PACKAGE"

FROM alpine
COPY --from=builder /usr/local/bin/drone /usr/local/bin/drone
CMD [ "drone" ]
