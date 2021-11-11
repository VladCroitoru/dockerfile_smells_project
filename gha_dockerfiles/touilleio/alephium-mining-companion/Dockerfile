FROM --platform=$BUILDPLATFORM golang as builder

ARG TARGETOS
ARG TARGETARCH
ARG VERSION
ARG BUILD_DATE

COPY . /src

WORKDIR /src

RUN env GOOS=${TARGETOS} GOARCH=${TARGETARCH} CGO_ENABLED=0 go mod download && \
  export GIT_COMMIT=$(git rev-parse HEAD) && \
  export GIT_DIRTY=$(test -n "`git status --porcelain`" && echo "+CHANGES" || true) && \
  env GOOS=${TARGETOS} GOARCH=${TARGETARCH} CGO_ENABLED=0 \
    go build -o alephium-mining-companion \
    -ldflags "-X github.com/sqooba/go-common/version.GitCommit=${GIT_COMMIT}${GIT_DIRTY} \
              -X github.com/sqooba/go-common/version.BuildDate=${BUILD_DATE} \
              -X github.com/sqooba/go-common/version.Version=${VERSION}" \
    .

FROM --platform=$BUILDPLATFORM gcr.io/distroless/base

COPY --from=builder /src/alephium-mining-companion /alephium-mining-companion

USER nobody

ENTRYPOINT ["/alephium-mining-companion"]
EXPOSE 8080

HEALTHCHECK --interval=60s --timeout=10s --retries=1 --start-period=30s CMD ["/alephium-mining-companion", "--health-check"]
