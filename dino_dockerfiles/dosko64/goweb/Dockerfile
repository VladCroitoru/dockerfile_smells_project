# build stage
FROM golang:alpine AS build-env
RUN  apk update && apk add git
ADD . /src
RUN go install github.com/dosko64/goweb@latest

# final stage
FROM alpine
WORKDIR /app
COPY --from=build-env /go/bin/goweb /app/
ENTRYPOINT ./goweb
