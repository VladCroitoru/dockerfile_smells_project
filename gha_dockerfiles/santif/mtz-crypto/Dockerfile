ARG GO_VERSION=1.17

# STAGE 1: build - creación del archivo ejecutable
FROM golang:${GO_VERSION}-alpine AS build

RUN apk add --no-cache git

WORKDIR /work
ADD cmd ./cmd
ADD pkg ./pkg
ADD go.mod ./go.mod
ADD go.sum ./go.sum

RUN CGO_ENABLED=0 go build -o /service ./cmd/mtz-crypto-service

# STAGE 2: imagen de salida, con el servicio ejecutable
FROM gcr.io/distroless/static AS final

ARG SVC_NAME
ARG APP_VSN
ARG GIT_COMMIT
ARG BUILD_DATE

USER nonroot:nonroot
 
COPY --from=build --chown=nonroot:nonroot /service /service

ENV MTZ_CRYPTO_LOGGING_FORMAT="json" \
    VERSION=${APP_VSN}

EXPOSE 8000/tcp

ENTRYPOINT ["/service"]

# ----------------------------------------------------------------------------------------
# IMPORTANTE: Mantener estas líneas al FINAL del archivo
# ----------------------------------------------------------------------------------------
LABEL org.opencontainers.image.url="https://github.com/matbarofex/mtz-crypto" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.vendor="Matriz SA" \
      org.opencontainers.image.licenses="MIT" \
      org.opencontainers.image.ref.name="mtzio/mtz-crypto" \
      org.opencontainers.image.title="mtz-crypto" \
      org.opencontainers.image.description="Servicio de ejemplo para capacitación Go" \
      org.opencontainers.image.revision="${GIT_COMMIT}" \
      org.opencontainers.image.created="${BUILD_DATE}"
# ----------------------------------------------------------------------------------------
