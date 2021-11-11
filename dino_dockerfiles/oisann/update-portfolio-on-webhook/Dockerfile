FROM golang:1.10-alpine as builder
WORKDIR /go/src/oisann.net/update-portfolio-on-webhook
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

FROM scratch
WORKDIR /root/
COPY --from=builder /go/src/oisann.net/update-portfolio-on-webhook/main .
CMD ["./main"]