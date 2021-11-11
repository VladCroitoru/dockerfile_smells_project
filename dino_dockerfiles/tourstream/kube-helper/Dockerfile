FROM golang:1.9 as builder
RUN go get -u github.com/golang/dep
RUN go install github.com/golang/dep/cmd/dep

WORKDIR /go/src/kube-helper/
COPY . .
ADD https://github.com/upx/upx/releases/download/v3.94/upx-3.94-amd64_linux.tar.xz .
RUN apt-get update  && apt-get install xz-utils
RUN tar -xf upx-3.94-amd64_linux.tar.xz
RUN dep ensure
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -a -installsuffix cgo -o kube-helper .
RUN upx-3.94-amd64_linux/upx --best --ultra-brute kube-helper

FROM scratch
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /go/src/kube-helper/kube-helper /
ENTRYPOINT ["/kube-helper"]