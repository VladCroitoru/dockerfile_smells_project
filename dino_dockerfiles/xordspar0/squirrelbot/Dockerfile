FROM golang:1.9.2-alpine3.6 AS build

# Install build tools.
RUN apk add --no-cache git make

# Copy and build squirrelbot.
COPY . /src/squirrelbot/
WORKDIR /src/squirrelbot/
RUN make build

FROM alpine:latest
# Install runtime dependencies.
RUN apk --update --no-cache add \
  ca-certificates \
  youtube-dl

COPY --from=build /src/squirrelbot/build/squirrelbot /usr/local/bin/squirrelbot
CMD ["/usr/local/bin/squirrelbot"]
