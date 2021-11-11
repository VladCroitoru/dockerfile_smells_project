ARG go_version=1.14-alpine
FROM golang:$go_version AS build

WORKDIR /app

COPY $PWD/go.mod /app
COPY $PWD/go.sum /app
RUN go mod download

COPY $PWD /app
RUN CGO_ENABLED=0 go build -o weather-exporter

FROM scratch AS run

WORKDIR /app
COPY --from=build /app/weather-exporter /usr/bin/weather-exporter
COPY --from=build /etc/ssl/certs /etc/ssl/certs
EXPOSE 8080
ENTRYPOINT ["/usr/bin/weather-exporter"]
