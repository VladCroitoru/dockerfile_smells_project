FROM golang:1.9-alpine as builder
WORKDIR /go/src/kube2clouddns
RUN apk --no-cache add glide git
COPY glide.* ./
RUN glide install
COPY *.go ./
RUN go build -v

FROM alpine:3.6
COPY --from=builder /go/src/kube2clouddns/kube2clouddns /usr/bin/

ENTRYPOINT ["kube2clouddns"]
