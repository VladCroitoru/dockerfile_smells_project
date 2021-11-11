# ------------------------------------------------------------------------------
# Builder Image
# ------------------------------------------------------------------------------
FROM golang AS build

WORKDIR /go/src/github.com/figment-networks/terra-worker/

COPY ./go.mod .
COPY ./go.sum .

RUN go mod download

COPY .git .git
COPY ./Makefile ./Makefile
COPY ./api ./api
COPY ./client ./client
COPY ./cmd/common ./cmd/common
COPY ./cmd/terra-worker ./cmd/terra-worker


ENV GOARCH=amd64
ENV GOOS=linux

RUN \
  GO_VERSION=$(go version | awk {'print $3'}) \
  GIT_COMMIT=$(git rev-parse HEAD) \
  make build

# ------------------------------------------------------------------------------
# Target Image
# ------------------------------------------------------------------------------
# FROM alpine:3.10 AS release  CANNOT BE ALPINE BECAUSE OF COSMWASM
FROM golang AS release

WORKDIR /app/terra
RUN adduser --system --uid 1234 figment
COPY --from=build /go/src/github.com/figment-networks/terra-worker/worker /app/terra/worker
COPY --from=build /go/pkg/mod/github.com/\!cosm\!wasm/wasmvm@v0.16.0/api/libwasmvm.so /app/terra/lib/libwasmvm.so
RUN chmod a+x ./worker
ENV LD_LIBRARY_PATH=/app/terra/lib
RUN chown -R figment /app/
USER 1234
CMD ["./worker"]
