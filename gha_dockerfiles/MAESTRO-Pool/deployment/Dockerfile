FROM debian:stable-slim as cardano-node

# timezone
ENV TZ=US/Pacific
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# system dependencies
RUN apt-get update -y
RUN apt-get install -y \
    automake \
    build-essential \
    pkg-config \
    libffi-dev \
    libgmp-dev \
    libssl-dev \
    libtinfo-dev \
    libsystemd-dev \
    zlib1g-dev \
    make \
    g++ \
    tmux \
    git \
    jq \
    wget \
    libncursesw5 \
    libtool \
    autoconf


# cabal
ENV CABAL_VERSION=3.2.0.0
ENV PATH="/root/.cabal/bin:/root/.ghcup/bin:/root/.local/bin:$PATH"
RUN wget https://downloads.haskell.org/~cabal/cabal-install-${CABAL_VERSION}/cabal-install-${CABAL_VERSION}-x86_64-unknown-linux.tar.xz \
    && tar -xf cabal-install-${CABAL_VERSION}-x86_64-unknown-linux.tar.xz \
    && rm cabal-install-${CABAL_VERSION}-x86_64-unknown-linux.tar.xz cabal.sig \
    && mkdir -p ~/.local/bin \
    && mv cabal ~/.local/bin/ \
    && cabal update && cabal --version

# GHC
ENV GHC_VERSION=8.10.4
RUN wget https://downloads.haskell.org/ghc/${GHC_VERSION}/ghc-${GHC_VERSION}-x86_64-deb9-linux.tar.xz \
    && tar -xf ghc-${GHC_VERSION}-x86_64-deb9-linux.tar.xz \
    && rm ghc-${GHC_VERSION}-x86_64-deb9-linux.tar.xz \
    && cd ghc-${GHC_VERSION} \
    && ./configure \
    && make install \
    && cd / \
    && rm -rf /ghc-${GHC_VERSION}

# Libsodium
RUN git clone https://github.com/input-output-hk/libsodium && \
    cd libsodium && \
    git checkout 66f017f1 && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make install
ENV LD_LIBRARY_PATH="/usr/local/lib:$LD_LIBRARY_PATH"
ENV PKG_CONFIG_PATH="/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH"

# Install cardano-node
ENV NODE_VERSION=1.30.1
RUN echo "Building tags/${NODE_VERSION}..." \
    && echo tags/${NODE_VERSION} > /CARDANO_BRANCH \
    && git clone https://github.com/input-output-hk/cardano-node.git \
    && cd cardano-node \
    && git fetch --all --recurse-submodules --tags \
    && git tag \
    && git checkout tags/${NODE_VERSION} \
    && cabal configure --with-compiler=ghc-$GHC_VERSION \
    && echo "package cardano-crypto-praos" >>  cabal.project.local \
    && echo "  flags: -external-libsodium-vrf" >>  cabal.project.local \
    && cabal build all \
    && mkdir -p /root/.local/bin/ \
    && cp -p dist-newstyle/build/x86_64-linux/ghc-$GHC_VERSION/cardano-node-${NODE_VERSION}/x/cardano-node/build/cardano-node/cardano-node /root/.local/bin/ \
    && cp -p dist-newstyle/build/x86_64-linux/ghc-$GHC_VERSION/cardano-cli-${NODE_VERSION}/x/cardano-cli/build/cardano-cli/cardano-cli /root/.local/bin/ \
    && rm -rf /root/.cabal/packages \
    && rm -rf /usr/local/lib/ghc-8.6.5/ \
    && rm -rf /cardano-node/dist-newstyle/ \
    && rm -rf /root/.cabal/store/ghc-8.6.5

# Copy runner
COPY config /cardano/cardano-node
COPY scripts/runner.sh /cardano/

RUN apt-get install tcptraceroute procps curl vim lsof bc -y
RUN curl -s -o gLiveView.sh https://raw.githubusercontent.com/cardano-community/guild-operators/master/scripts/cnode-helper-scripts/gLiveView.sh
RUN curl -s -o env https://raw.githubusercontent.com/cardano-community/guild-operators/master/scripts/cnode-helper-scripts/env
RUN chmod 755 gLiveView.sh

ENV CARDANO_NODE_SOCKET_PATH /cardano/cardano-node/db/node.socket
# ARG node-type
RUN chmod +x /cardano/runner.sh
# CMD [ "/cardano/runner.sh", "cardano-node", "/cardano", ${node-type} ]


FROM cardano-node as key-generator
WORKDIR /generate
RUN wget https://github.com/input-output-hk/cardano-wallet/releases/download/v2021-08-27/cardano-wallet-v2021-08-27-linux64.tar.gz
RUN tar -xvf cardano-wallet-v2021-08-27-linux64.tar.gz && \
    rm cardano-wallet-v2021-08-27-linux64.tar.gz
ENV PATH "${PATH}:/generate/cardano-wallet-v2021-08-27"
COPY generateOwnerKeys.sh /generate
RUN chmod +x generateOwnerKeys.sh
