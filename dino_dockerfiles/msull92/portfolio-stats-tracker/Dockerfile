FROM golang:1.8 as builder
WORKDIR /go/src/github.com/msull92/portfolio-stats-tracker
COPY *.go ./
RUN go get ./...
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /go/src/github.com/msull92/portfolio-stats-tracker/main .
CMD ["./main"]
