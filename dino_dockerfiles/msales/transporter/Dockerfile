# Build container
FROM golang:1.9 as builder

RUN go get -u github.com/golang/dep/cmd/dep

WORKDIR /go/src/github.com/msales/transporter/
COPY ./ .
RUN dep ensure

RUN CGO_ENABLED=0 GOOS=linux go build -a -ldflags '-s' -o transporter ./cmd/transporter

# Run container
FROM scratch

COPY --from=builder /go/src/github.com/msales/transporter/transporter .

ENV TRANSPORTER_PORT "80"

EXPOSE 80
CMD ["./transporter", "server"]