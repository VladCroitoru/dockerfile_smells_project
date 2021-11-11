# Build
FROM golang:1.9 AS build
WORKDIR /go/src/github.com/target/jenkins-docker-api
ENV CGO_ENABLED=0 GOOS=linux

COPY cmd ./cmd/
COPY docker ./docker/
COPY fixtures ./fixtures/
COPY github ./github/
COPY router ./router/
COPY server ./server/
COPY util ./util/
COPY version ./version/
COPY vendor ./vendor/

RUN go build -o jenkins-server -a -installsuffix go ./cmd/jenkins-server

# Application
FROM alpine:latest
EXPOSE 8080
COPY --from=build /go/src/github.com/target/jenkins-docker-api/jenkins-server /
CMD ["/jenkins-server"]
