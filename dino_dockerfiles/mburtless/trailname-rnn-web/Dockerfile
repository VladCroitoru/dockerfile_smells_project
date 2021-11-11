# Build stage
FROM golang:1.8 AS build-env
COPY . /go/src/github.com/mburtless/trailname-rnn-web
RUN cd /go/src/github.com/mburtless/trailname-rnn-web/cmd/trailname-rnn-web && CGO_ENABLED=0 GOOS=linux go build -o trailname-rnn-web .

# Final stage
FROM alpine:latest
WORKDIR /app
COPY --from=build-env /go/src/github.com/mburtless/trailname-rnn-web/cmd/trailname-rnn-web/trailname-rnn-web .
COPY --from=build-env /go/src/github.com/mburtless/trailname-rnn-web/web ./web
# Copy data needed for wordsegmentation
COPY --from=build-env /go/src/github.com/mburtless/trailname-rnn-web/vendor/github.com/AntoineAugusti/wordsegmentation/data ./src/github.com/AntoineAugusti/wordsegmentation/data
ENV APIHOST=localhost:6788
ENV PORT=8000
# Must set GOPATH for wordsegmenation to run
ENV GOPATH=/app
EXPOSE 8000
CMD ["./trailname-rnn-web"]
