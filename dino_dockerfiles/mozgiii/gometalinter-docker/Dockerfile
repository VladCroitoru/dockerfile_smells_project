FROM golang as builder

RUN go get -u github.com/alecthomas/gometalinter \
 && gometalinter --install --vendored-linters \
 && mv /go/bin/* /usr/local/bin/ \
 && rm -rf /go/pkg /go/*/*

CMD [ "gometalinter", "--vendor", "./..." ]
