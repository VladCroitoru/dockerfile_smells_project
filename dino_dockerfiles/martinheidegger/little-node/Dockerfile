FROM alpine:latest

WORKDIR /usr/src/app

ENV BUNDLE_PATH=/usr/local/bundle

# for node and/or package builds: gcc g++ libgcc binutils-gold linux-headers make openssl openssh-client python
# for node/npm installs: curl git
# for npm installation and other use-cases: tar
# for packages: man
# for ci: bash
# for mounted volume permissions: su-exec
RUN mkdir -p /usr/src/app \
    && apk update \
    && apk add --no-cache make bash gcc g++ man linux-headers curl git openssl openssh-client \
                          python binutils-gold gnupg tar libgcc su-exec \
    ## For the build of node
    && curl -sL https://raw.githubusercontent.com/martinheidegger/install-node/master/install_node.sh | \
       NODE_VERSION="v8.1.2" \
       NODE_VARIANT="make" \
       bash \
    && npm i npm@latest -g \
    && rm -rf /var/lib/apt/lists/* /usr/share/perl* || true

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
