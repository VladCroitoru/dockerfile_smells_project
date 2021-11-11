FROM golang:1.17 as builder

WORKDIR /go/src/github.com/project0/certjunkie/

COPY . .
RUN go get -v

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -ldflags '-w' -o certjunkie .

FROM scratch

WORKDIR /root/

COPY --from=builder /etc/ssl/certs /etc/ssl/certs
COPY --from=builder /go/src/github.com/project0/certjunkie/certjunkie .

ENTRYPOINT ["./certjunkie"]

CMD [ "server" ]