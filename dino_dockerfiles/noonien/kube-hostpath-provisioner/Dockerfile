FROM golang:1.9 as builder
WORKDIR /go/src/github.com/noonien/kube-hostpath-provisioner
COPY . .
RUN go build

FROM bitnami/minideb:latest
COPY --from=builder /go/src/github.com/noonien/kube-hostpath-provisioner/kube-hostpath-provisioner .
ENTRYPOINT ["/kube-hostpath-provisioner"]
