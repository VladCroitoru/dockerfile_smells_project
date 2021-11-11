# Stage 1 buiding
FROM golang:1.10 as BUILDER

LABEL maintainer="antmanler(wo@zhaob.in)"

COPY . /go/src/github.com/antmanler/gnatsd-jwt
WORKDIR /go/src/github.com/antmanler/gnatsd-jwt

RUN CGO_ENABLED=0 go install -v -a -tags netgo -installsuffix netgo -ldflags "-s -w -X github.com/nats-io/gnatsd/version.GITCOMMIT=`git rev-parse --short HEAD`+jwt"

FROM alpine:latest
RUN apk --no-cache add ca-certificates

WORKDIR /root/
COPY --from=builder /go/bin/gnatsd-jwt gnatsd
EXPOSE 4222 8222
ENTRYPOINT ["/root/gnatsd"]
CMD ["--help"]
