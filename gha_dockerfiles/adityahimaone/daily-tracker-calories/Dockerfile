#builder
FROM golang:1.16-alpine AS builder

RUN apk update && apk upgrade && \
    apk --update add git make
WORKDIR /app
COPY . .
RUN go mod tidy
RUN go build -o mainrun

#runner
FROM alpine:latest
RUN apk --no-cache add ca-certificates
RUN apk update && apk upgrade && \
    apk --update --no-cache add tzdata && \
    mkdir /app

WORKDIR /app

STOPSIGNAL SIGINT
EXPOSE 8080
COPY --from=builder /app/mainrun /app
COPY --from=builder /app/app/config/ /app/app/config/
CMD /app/mainrun


