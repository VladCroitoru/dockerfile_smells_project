FROM golang:1-alpine as builder

RUN apk --update upgrade \
&& apk --no-cache --no-progress add git make \
&& rm -rf /var/cache/apk/*

WORKDIR /go/gallienii
COPY . .

RUN go mod download
RUN make build

FROM alpine:3
RUN apk --update upgrade \
    && apk --no-cache --no-progress add ca-certificates \
    && rm -rf /var/cache/apk/*

COPY --from=builder /go/gallienii/gallienii /usr/bin/gallienii

ENTRYPOINT ["/usr/bin/gallienii"]
