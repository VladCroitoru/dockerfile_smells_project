FROM golang:1.9.2-alpine AS goBuild
RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh && \
    go get -u -d github.com/mattes/migrate/cli github.com/go-sql-driver/mysql && \
    go build -tags 'mysql' -o /usr/local/bin/migrate github.com/mattes/migrate/cli

FROM alpine:3.6
COPY --from=goBuild /usr/local/bin/migrate /usr/local/bin/migrate
WORKDIR /migrations
RUN apk update && apk upgrade && apk add --no-cache openssh mysql-client
COPY entrypoint.sh /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
