FROM golang:latest
WORKDIR /go/src/github.com/pwillie/kube-cert-manager/
RUN curl https://glide.sh/get | sh
ADD . .
RUN glide install && ./build.sh

FROM alpine:latest  
RUN apk --no-cache add ca-certificates
WORKDIR /
COPY --from=0 /go/src/github.com/pwillie/kube-cert-manager/kube-cert-manager .
ENTRYPOINT ["/kube-cert-manager"]
