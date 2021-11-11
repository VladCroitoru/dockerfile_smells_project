FROM golang:1.16 as builder
COPY . src/
RUN cd src && go build -v -o app

FROM centos:centos8
COPY --from=builder /go/src/app .
RUN dnf install -y iproute curl bind-utils && dnf clean all
CMD ["/app"]
HEALTHCHECK CMD curl --fail http://localhost:8080/health || exit 1
