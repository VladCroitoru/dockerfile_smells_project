FROM golang:1.17-alpine AS builder
ENV CGO_ENABLED=0

RUN apk --no-cache add ca-certificates

WORKDIR /go/src/gitlab.com/jonny7/quetzal

COPY . .

RUN go mod download
RUN go build -o quetzal ./cmd/quetzal

EXPOSE 7838

FROM scratch

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /go/src/gitlab.com/jonny7/quetzal/quetzal ./quetzal

CMD ["./quetzal"]