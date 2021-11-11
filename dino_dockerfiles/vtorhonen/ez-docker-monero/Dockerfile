FROM debian:jessie-slim as builder
MAINTAINER Ville Törhönen <ville@torhonen.fi>

ENV MONERO_VERSION 0.11.0.0
ENV MONERO_SHA256 fa7742c822f3c966aa842bf20a9920803d690d9db02033d9b397cefc7cc07ff4

# Install dependencies
# Separate layer so we can cache things
RUN set -x && \
    apt-get update && \
    apt-get install -y \
        curl \
        bzip2 && \
    rm -rf /var/lib/apt/lists/*

# Download the binary and verify hash
RUN set -x && \
    cd /tmp && \
    curl -sLOJ https://downloads.getmonero.org/cli/monero-linux-x64-v${MONERO_VERSION}.tar.bz2 && \
    echo "${MONERO_SHA256} monero-linux-x64-v${MONERO_VERSION}.tar.bz2' | sha256sum -c" && \
    tar xf monero-linux-x64-v${MONERO_VERSION}.tar.bz2 && \
    mv monero-v${MONERO_VERSION} monero && \
    rm -f monero-linux-x64-v${MONERO_VERSION}.tar.bz2

# Copy binaries and libs from builder to a separate image
FROM debian:jessie-slim
MAINTAINER Ville Törhönen <ville@torhonen.fi>

COPY --from=builder /tmp/monero/monerod /usr/local/bin
COPY --from=builder /tmp/monero/monero-wallet-cli /usr/local/bin
COPY docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT [ "/docker-entrypoint.sh" ]
