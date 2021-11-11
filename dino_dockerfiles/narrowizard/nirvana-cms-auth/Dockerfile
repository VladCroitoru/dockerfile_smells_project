FROM golang:1.12 as builder
WORKDIR /go/src/nirvana-cms-auth
COPY . .
RUN go get
RUN CGO_ENABLED=0 GOOS=linux go build -a -v -o nirvana-cms-auth .

FROM alpine:latest
VOLUME ["/root/config","/root/log"]
WORKDIR /root/
EXPOSE 80
COPY --from=builder /go/src/nirvana-cms-auth/nirvana-cms-auth .
COPY --from=builder /go/src/nirvana-cms-auth/zoneinfo.zip /usr/local/go/lib/time/zoneinfo.zip
CMD ["/bin/sh","-c","./nirvana-cms-auth >> log/nirvana-cms-auth 2>&1"]