FROM golang:1.9
WORKDIR /go/src/github.com/uroshercog/k8s-secret-restart-controller/
ENV GOPATH /go
COPY vendor vendor
COPY pkg pkg
COPY main.go .
RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -a .

FROM alpine:3.7
WORKDIR /bin
COPY --from=0 /go/src/github.com/uroshercog/k8s-secret-restart-controller/k8s-secret-restart-controller k8s-secret-restart-controller
ENTRYPOINT ["/bin/k8s-secret-restart-controller"]
