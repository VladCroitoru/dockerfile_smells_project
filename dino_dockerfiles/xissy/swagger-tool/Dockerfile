# build stage
FROM golang:alpine AS build-env
RUN apk update; apk add git
RUN go get -u github.com/golang/dep/cmd/dep
ADD . /go/src/github.com/xissy/swagger-tool
WORKDIR /go/src/github.com/xissy/swagger-tool
RUN dep ensure
RUN go build -o swagger-tool

# final stage
FROM alpine
WORKDIR /app
COPY --from=build-env /go/src/github.com/xissy/swagger-tool/swagger-tool /app/
ENTRYPOINT ["./swagger-tool"]
