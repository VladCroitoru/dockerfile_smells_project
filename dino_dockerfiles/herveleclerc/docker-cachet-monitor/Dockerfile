FROM golang:1.6

MAINTAINER <herve leclerc> herve.leclerc@alterway.fr

RUN mkdir /app \
    && git clone https://github.com/CastawayLabs/cachet-monitor.git

WORKDIR cachet-monitor

RUN go get -v github.com/castawaylabs/cachet-monitor \
    && go build -o /app/cachet-monitor cli/main.go  \
    && cp example.config.json /app/.

CMD ["-c", "/app/example.config.json"]

ENTRYPOINT ["/app/cachet-monitor"]
