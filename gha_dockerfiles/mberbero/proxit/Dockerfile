FROM golang:1.16.6 as builder

RUN apt-get update && apt-get install -y xz-utils && rm -rf /var/lib/apt/lists/*
ADD https://github.com/upx/upx/releases/download/v3.96/upx-3.96-amd64_linux.tar.xz /usr/local
RUN xz -d -c /usr/local/upx-3.96-amd64_linux.tar.xz | tar -xOf - upx-3.96-amd64_linux/upx > /bin/upx && chmod a+x /bin/upx

WORKDIR /go/src/proxit

COPY . .

RUN go get .

RUN CGO_ENABLED=0 GOOS=linux go build -a -ldflags="-s -w" -installsuffix cgo  .
RUN strip --strip-unneeded proxit
RUN upx proxit


FROM alpine

RUN apk add nano wget curl nano bash

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

WORKDIR /bin/proxit

COPY --from=builder /go/src/proxit/services.yml .

COPY --from=builder /go/src/proxit/proxit .

CMD [ "./proxit" ]

EXPOSE 80
EXPOSE 443