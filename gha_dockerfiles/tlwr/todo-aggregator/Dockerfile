ARG go_version=1.16-alpine
FROM golang:$go_version AS build

WORKDIR /app

COPY $PWD/go.mod /app
COPY $PWD/go.sum /app
RUN go mod download

COPY $PWD /app
RUN CGO_ENABLED=0 go build -o todo-aggregator

FROM scratch AS run
WORKDIR /opt/todo-aggregator

COPY --from=build /app/todo-aggregator /usr/bin/todo-aggregator

COPY --from=build /app/public /opt/todo-aggregator/public
COPY --from=build /app/templates /opt/todo-aggregator/templates

COPY --from=build /etc/ssl/certs /etc/ssl/certs

EXPOSE 8080
ENTRYPOINT ["/usr/bin/todo-aggregator"]
