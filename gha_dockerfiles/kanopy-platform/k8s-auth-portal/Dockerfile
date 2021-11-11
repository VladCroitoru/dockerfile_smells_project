FROM golang:1.16 as build
WORKDIR /go/src/app
COPY . .
RUN go get -d -v ./...
RUN go build -o /go/bin/app

FROM debian:buster-slim
RUN apt-get update && apt-get install --yes ca-certificates
RUN groupadd -r app && useradd --no-log-init -r -g app app
USER app
COPY --from=build /go/bin/app /
ENV APP_ADDR ":8080"
EXPOSE 8080
ENTRYPOINT ["/app"]
