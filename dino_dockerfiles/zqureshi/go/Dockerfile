FROM golang:alpine AS builder
ADD . /go/src/github.com/zqureshi/go
WORKDIR /go/src/github.com/zqureshi/go
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /app/go .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
COPY --from=builder /app/go /app/
CMD ["/app/go"]
