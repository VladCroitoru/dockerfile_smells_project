# Build container
FROM golang:1.13 as builder

# Optional github secrets
ARG GITHUB_TOKEN
ENV GO111MODULE on


WORKDIR /app/double-team/
COPY ./ .

RUN test -n "${GITHUB_TOKEN}" && \
    git config --global url."https://${GITHUB_TOKEN}@github.com/".insteadOf "https://github.com/" || \
    true

RUN go test ./...

RUN CGO_ENABLED=0 GOOS=linux go build -a -ldflags "-s -X main.Version=$(git describe --tags --always)" -o double-team ./cmd/double-team

# Run container
FROM msales/alpine-base:3.8

COPY --from=builder /app/double-team .
COPY --from=builder /etc/ssl/certs /etc/ssl/certs

ENV DOUBLE_TEAM_PORT "80"

EXPOSE 80
CMD ["./double-team", "server"]
