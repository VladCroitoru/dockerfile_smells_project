FROM golang:1.16-alpine as builder
RUN apk add --no-cache \
    git

WORKDIR /app
COPY . /app
RUN env CGO_ENABLED=0 \
    go build -a -o /casecmp -ldflags "-s -w \
        -X main.version=$(cat VERSION) \
        -X main.commit=$(git show --format='%h' --no-patch) \
        -X main.date=$(date +%Y-%m-%dT%T%z)"

FROM scratch
COPY --from=builder /casecmp /
ENV PORT 8080
EXPOSE 8080
WORKDIR /
ENTRYPOINT ["/casecmp"]
