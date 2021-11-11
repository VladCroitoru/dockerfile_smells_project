FROM golang:1.10 as builder
WORKDIR /usr/local/go/src/github.com/hagen1778/gif-generator
ADD . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM scratch
COPY --from=builder /usr/local/go/src/github.com/hagen1778/gif-generator/app .
CMD ["./app"]