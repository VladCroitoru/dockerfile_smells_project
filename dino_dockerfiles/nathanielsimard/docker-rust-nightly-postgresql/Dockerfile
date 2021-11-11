FROM postgres

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    ca-certificates \
    curl \
    file \
    build-essential \
    openssl \
    libssl-dev \
    libpq-dev \
    pkg-config \
    autoconf \
    automake \
    autotools-dev \
    libtool \
    xutils-dev \
    && \
    rm -rf /var/lib/apt/lists/*

RUN curl https://sh.rustup.rs -sSf | \
    sh -s -- --default-toolchain nightly -y

ENV PATH=/root/.cargo/bin:$PATH