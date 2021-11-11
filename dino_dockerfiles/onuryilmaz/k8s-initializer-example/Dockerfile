FROM golang:1.9 as builder
ADD . /go/src/github.com/onuryilmaz/k8s-initializer-example/
WORKDIR /go/src/github.com/onuryilmaz/k8s-initializer-example/
RUN GOOS=linux go build -o initializer

FROM scratch as packager
COPY --from=builder /go/src/github.com/onuryilmaz/k8s-initializer-example/initializer /initializer
ENTRYPOINT ["./initializer"]