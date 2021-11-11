FROM golang:1.17 as builder
WORKDIR /go/src/github.com/ancientlore/hashsrv
COPY . .
WORKDIR /go/src/github.com/ancientlore/hashsrv/cmd/hashsrv
RUN go version
RUN CGO_ENABLED=0 GOOS=linux GO111MODULE=on go get .
RUN CGO_ENABLED=0 GOOS=linux GO111MODULE=on go install

FROM ancientlore/goimg:latest
COPY hashsrv.config /go/etc/hashsrv.config
COPY --from=builder /go/bin/hashsrv /usr/bin/hashsrv
EXPOSE 9009
ENTRYPOINT ["/usr/bin/hashsrv", "-run"]
