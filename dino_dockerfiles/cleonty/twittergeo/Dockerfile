FROM golang:1.13-alpine AS builder
WORKDIR /go/src/app
COPY . .
RUN go build -o twittergeo

FROM alpine:latest  
WORKDIR /root/
COPY --from=builder /go/src/app/twittergeo .
EXPOSE 8383
CMD ["./twittergeo"]