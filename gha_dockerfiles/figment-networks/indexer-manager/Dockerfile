# ------------------------------------------------------------------------------
# Builder Image
# ------------------------------------------------------------------------------
FROM golang AS build

WORKDIR /build

COPY ./go.mod .
COPY ./go.sum .

RUN go mod download

COPY .git .git
COPY ./Makefile ./Makefile
COPY ./manager ./manager
COPY ./conn ./conn
COPY ./cmd/common ./cmd/common
COPY ./cmd/manager ./cmd/manager

ENV CGO_ENABLED=0
ENV GOARCH=amd64
ENV GOOS=linux

RUN \
  GO_VERSION=$(go version | awk {'print $3'}) \
  GIT_COMMIT=$(git rev-parse HEAD) \
  make build

# ------------------------------------------------------------------------------
# Target Image
# ------------------------------------------------------------------------------
FROM alpine  AS release

RUN addgroup --gid 1234 figment
RUN adduser --system --uid 1234 figment
USER 1234
WORKDIR /app

COPY --from=build  /build/manager_bin /app/manager
CMD ["/app/manager"]
