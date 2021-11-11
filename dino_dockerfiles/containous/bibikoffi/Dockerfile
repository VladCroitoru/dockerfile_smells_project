FROM golang:1-alpine as builder

RUN apk --update upgrade \
&& apk --no-cache --no-progress add git make \
&& rm -rf /var/cache/apk/*

WORKDIR /go/src/github.com/traefik/bibikoffi
COPY . .

RUN go mod download
RUN make build

FROM alpine:3.6
RUN apk --update upgrade \
    && apk --no-cache --no-progress add ca-certificates \
    && rm -rf /var/cache/apk/*

COPY --from=builder /go/src/github.com/traefik/bibikoffi/bibikoffi /usr/bin/bibikoffi

ENTRYPOINT ["/usr/bin/bibikoffi"]
