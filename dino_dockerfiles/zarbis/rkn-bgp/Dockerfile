FROM golang:1.10-alpine as builder
WORKDIR /go/src/app
RUN apk -U add ca-certificates
COPY . .
RUN CGO_ENABLED=0 go build

FROM scratch
COPY --from=builder /etc/ssl/certs /etc/ssl/certs
COPY --from=builder /go/src/app/app .
ENTRYPOINT ["/app"]
