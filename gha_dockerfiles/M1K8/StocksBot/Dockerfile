# Build stage
FROM golang:1.17.1 as build-env
WORKDIR /src/discordstocksbot
ADD . /src/discordstocksbot
ENV CGO_ENABLED=0
RUN go get -d -v -u ./...
RUN go mod vendor
RUN cd ./cmd/discordstocksbot && go build -o /app

FROM gcr.io/distroless/base:latest
COPY --from=build-env /app /
ENV FINNHUB_API="-"
ENV DISCORD_API="-"

ENV TWITTER_C_K="-"
ENV TWITTER_C_S="-"

ENV TWITTER_A_T="-"
ENV TWITTER_A_S="-"

CMD ["/app"]
