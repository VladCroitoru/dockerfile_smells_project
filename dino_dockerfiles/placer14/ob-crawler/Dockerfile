FROM golang:1.8.1
WORKDIR /go/src/github.com/placer14/ob-crawler
RUN go get gopkg.in/jarcoal/httpmock.v1
COPY . .
RUN go test ./... && \
  CGO_ENABLED=0 GOOS=linux go build -a -ldflags '-extldflags "-static"' -o /opt/ob-crawler .

FROM scratch
WORKDIR /opt
COPY --from=0 /opt/ob-crawler /opt/ob-crawler
ENTRYPOINT ["/opt/ob-crawler"]
CMD ["-help"]

