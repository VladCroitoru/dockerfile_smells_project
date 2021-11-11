FROM golang:alpine as build
RUN apk add --no-cache ca-certificates
WORKDIR /app
COPY . .
RUN go build -o tsgen ./cmd/tsgen

FROM alpine:latest
RUN apk add --no-cache ca-certificates
COPY --from=build /app/tsgen /usr/local/bin/tsgen
EXPOSE 8080

ENTRYPOINT [ "tsgen" ]
CMD ["--config.file=/etc/tsgen/config.yml"]
