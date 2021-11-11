# build binary
FROM golang:1.10.3-alpine3.8 AS build
RUN apk add --no-cache linux-headers gcc g++
ARG VERSION=dev
WORKDIR /go/src/github.com/wenkaler/github-api
COPY . /go/src/github.com/wenkaler/github-api
RUN CGO_ENABLED=1 go build \
    -o /out/api \
    github.com/wenkaler/github-api/cmd

# copy to alpine image
FROM alpine:3.8
WORKDIR /app
RUN mkdir /db
COPY --from=build /out/api /app
RUN apk add --no-cache tzdata
RUN apk --no-cache add ca-certificates
ENV TZ Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
CMD ["/app/api"]
