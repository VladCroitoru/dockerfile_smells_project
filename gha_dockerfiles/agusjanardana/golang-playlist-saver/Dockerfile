#stage 1
FROM golang:1.17-alpine AS golang
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN go clean --modcache
RUN go build -o main

#stage 2
FROM alpine:3.14
WORKDIR /root/
COPY --from=golang /app/.env .
COPY --from=golang /app/main .
EXPOSE 8080
CMD ["./main"]
