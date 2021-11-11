FROM golang:1.9-alpine AS build

WORKDIR /go/src/github.com/pcfens/redirector
COPY . /go/src/github.com/pcfens/redirector

RUN apk add --no-cache ca-certificates git \
    && CGO_ENABLED=0 GOOS=linux go build -a -o redirector

FROM scratch

COPY *.yaml /
COPY --from=build /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=build /go/src/github.com/pcfens/redirector/redirector redirector

ENTRYPOINT ["/redirector"]
