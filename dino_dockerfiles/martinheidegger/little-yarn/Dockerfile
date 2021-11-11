FROM alpine:3.4

WORKDIR /usr/src/app

ENV BUNDLE_PATH=/usr/local/bundle
RUN mkdir -p /usr/src/app \
    && apk update \
    && apk add --no-cache \
       # For building Node and the packages
       make python linux-headers gcc g++ libgcc binutils-gold \
       # Execution of scripts in yarn run 
       bash \
       # For downloading install_node
       curl \
       # Installing git npm dependencies
       git \
       # Runtime dependency used by node for ssl & crypto operations
       gnupg openssl openssh-client \
    # Building the exact node & yarn version
    && curl -sL https://raw.githubusercontent.com/martinheidegger/install-node/master/install_node.sh | \
       NODE_VERSION="v7.6.0" \
       YARN_VERSION="v0.21.3" \
       NODE_VARIANT="make" \
       bash \
    # Curl not needed after the installation
    && apk del curl \
    # Clearing the installation (Don't result in error)
    && (rm -rf \
       /var/lib/apt/lists/* \
       # No need to keep the documentation
       /usr/share/doc \
       # No need to keep perl
       /usr/share/perl* \
       # No need to keep man files of build dependencies
       /usr/share/man \
       || true)
