# Build Go Server Binary
FROM golang:1.17.1-buster

ARG GITHUB_TOKEN=local
ARG VERSION=local

# GITHUB_TOKEN is used to fetch codes from private repository
RUN echo "machine github.com login ${GITHUB_TOKEN}" > ~/.netrc

WORKDIR /project

# Only copy go.mod and go.sum, and download go mods separately to support layer caching
COPY ./go.* ./
RUN go mod download

COPY . ./

RUN CGO_ENABLED=0 GOOS=linux go install -v \
            -ldflags="-w -s -X github.com/Fantamstick/go-example-api/pkg/version.Version=${VERSION}" \
            ./cmd/example-api/

# Build Docker with Only Server Binary
FROM alpine:latest

RUN apk --no-cache add ca-certificates

COPY --from=0 /go/bin/example-api /bin/server

RUN addgroup -g 1001 fantamstick && adduser -D -G fantamstick -u 1001 fantamstick

USER 1001

CMD ["/bin/server"]
