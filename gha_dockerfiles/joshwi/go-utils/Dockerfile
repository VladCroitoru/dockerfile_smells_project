FROM golang:1.16-alpine
WORKDIR /app
COPY go.mod ./
COPY go.sum ./
COPY graphdb/ ./graphdb
COPY parser/ ./parser
COPY utils/ ./utils
COPY cron/ ./cron
COPY main.go ./main.go
RUN ls -la
RUN go mod download
RUN go env GOOS GOARCH
RUN GOOS=linux GOARCH=arm64 go build -o ./nfldb_collector
RUN chmod 755 ./cron/entrypoint.sh
RUN /usr/bin/crontab ./cron/crontab.txt
WORKDIR /app/cron
CMD ["./entrypoint.sh"]