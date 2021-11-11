FROM alpine:latest
LABEL maintainer="Benjamin R. Haskell <docker@benizi.com>"

# Install binaries to somewhere not under /root/ (When using this as a builder,
# you can just copy this directory into the destination container)
ARG haskell_builder_prefix="/opt/bin"

# Enable "edge" repositories
RUN sed -i -e 's%[^/]*\(/[^/]*\)$%edge\1%' /etc/apk/repositories

# Things needed to build Haskell libraries
RUN apk add --no-cache ghc cabal curl musl-dev zlib-dev git linux-headers

# Install `stack`, but STFU about my rc files
RUN \
  curl -sSL https://get.haskellstack.org/ | \
  sed -e '/check_home_local/!b' -e '/ /b' -e 's/^/#/' | \
  sh

# Use system GHC on Alpine
RUN stack config set system-ghc --global true

# Install binaries into the shared prefix directory
RUN \
  set -e ; \
  mkdir -p "${haskell_builder_prefix}" ; \
  printf 'local-bin-path: %s\n' "${haskell_builder_prefix}" | \
  tee -a /root/.stack/config.yaml

# Add it to the default PATH
ENV PATH "${haskell_builder_prefix}:$PATH"

# Seed the cache with some common libs that have many deps
ARG resolver="lts-9.13"
ARG packages="conduit wreq"

# cache the downloads separately ...
RUN stack --resolver ${resolver} build --prefetch --dry-run ${packages}
# ... then build the selected packages
RUN stack --resolver ${resolver} build ${packages}
