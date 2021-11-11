FROM golang
WORKDIR /go/src/
RUN go get golang.org/x/net/context
RUN go get github.com/docker/docker/api
RUN go get github.com/docker/docker/client
RUN go get github.com/rancher/go-rancher/v2
RUN mkdir -p /go/src/github.com/weyield
COPY . /go/src/github.com/weyield/safer-rancher
WORKDIR /go/src/github.com/weyield/safer-rancher
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o safer-rancher databases.go rancher.go safer-rancher.go

FROM alpine
RUN apk add --no-cache ca-certificates
WORKDIR /root/
COPY --from=0 /go/src/github.com/weyield/safer-rancher/safer-rancher .
CMD ["./safer-rancher"]
