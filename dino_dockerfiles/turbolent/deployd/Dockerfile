FROM golang:latest
WORKDIR /go/src/github.com/turbolent/deployd
ADD . .
RUN CGO_ENABLED=0 GOOS=linux go build -v -a -o deployd .

FROM scratch
CMD ["/deployd"]
EXPOSE 7070
ADD https://curl.haxx.se/ca/cacert.pem /etc/ssl/certs/ca-certificates.crt
COPY --from=0 /go/src/github.com/turbolent/deployd/deployd /deployd
