FROM golang:1.13-buster as builder
MAINTAINER Justin C. Miller <justin@justin.cm>

ADD . /app
WORKDIR /app
RUN go build


FROM debian:buster-slim as runner

ENV PORT=8000
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*
COPY --from=builder /app/slackdice /app/slackdice

WORKDIR /app
CMD ["./slackdice"]
