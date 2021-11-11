FROM golang:1.16-alpine AS builder
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN go clean --modcache
RUN go build -o main

#stage 2
FROM alpine:3.14
WORKDIR /root/
COPY --from=builder /app/config.json .
COPY --from=builder /app/main .
EXPOSE 8080
CMD ["./main"]

# FROM golang:1.17-alpine AS build

# WORKDIR /app
# COPY go.mod .
# COPY go.sum .
# RUN go mod download

# COPY . .
# RUN go build -o app

# FROM alpine:latest
# COPY --from=build /app/app /app

# EXPOSE 8080
# CMD ["/app"]