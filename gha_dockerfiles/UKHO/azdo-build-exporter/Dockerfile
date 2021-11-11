FROM golang:1.14 AS builder
COPY . .
RUN go get -d -v .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o azdo-build-exporter .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
COPY --from=builder /go/azdo-build-exporter .
EXPOSE 8080
ENTRYPOINT ["./azdo-build-exporter"]