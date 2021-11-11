FROM golang:1.17 as builder
WORKDIR /go/src/github.com/ancientlore/served
COPY . .
RUN go version
RUN CGO_ENABLED=0 GOOS=linux GO111MODULE=on go get .
RUN CGO_ENABLED=0 GOOS=linux GO111MODULE=on go install

FROM ancientlore/goimg:latest
COPY demo.config /etc/served.config
COPY . /go/src/github.com/ancientlore/served
COPY --from=builder /go/bin/served /usr/bin/served
EXPOSE 8000
ENTRYPOINT ["/usr/bin/served", "-run"]
