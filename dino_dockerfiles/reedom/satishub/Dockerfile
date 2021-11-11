FROM reedom/golang-dep:go1.9.4-stretch-dep0.4.1 as builder

ARG LDFLAGS

WORKDIR /go/src/github.com/reedom/satishub
ADD Gopkg.toml Gopkg.toml
ADD Gopkg.lock Gopkg.lock
RUN dep ensure -vendor-only -v
ADD . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -ldflags "$LDFLAGS" -installsuffix cgo -o bin/satishub main.go

FROM alpine:3.7

WORKDIR /var/satishub

RUN apk update && apk add ca-certificates tini && rm -rf /var/cache/apk/*
COPY --from=builder /go/src/github.com/reedom/satishub/bin/satishub /usr/local/bin/satishub

EXPOSE 80
EXPOSE 443

ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/satishub"]
CMD ["-h"]
