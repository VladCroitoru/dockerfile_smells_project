FROM rust:1.41.1-buster

# Base dependencies
RUN apt-get update -qqy \
 && apt-get install -qqy --no-install-recommends \
    locales \
    libsodium23 \
    libsodium-dev \
    clang \
    make \
    cmake \
    meson \
    ninja-build \
    flex \
    bison \
    libc6-dbg \
    python3 \
    python3-pip \
    python3-setuptools \
    python3-wheel \
 && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# Fix locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8

# Add wrapper scripts
ADD saltyrtc-server-launcher /usr/local/bin/saltyrtc-server-launcher
ADD generate-cert.sh /saltyrtc/certs/generate-cert.sh

# Update permissions
RUN chmod a+w /saltyrtc && \
    chmod a+x /saltyrtc/certs/generate-cert.sh && \
    chmod a+x /usr/local/bin/saltyrtc-server-launcher

# Install SaltyRTC server
RUN pip3 install saltyrtc.server[logging]

# Install cargo-audit
RUN cargo install --git https://github.com/rustsec/cargo-audit --tag v0.13.1 --locked

# Install valgrind
RUN wget https://sourceware.org/pub/valgrind/valgrind-3.15.0.tar.bz2 && \
    tar xf valgrind-3.15.0.tar.bz2 && \
    cd valgrind-3.15.0 && \
    ./configure && \
    make && \
    make install

# Install splint
#
# Debian package seems broken, results in parse error.
# Build instructions taken from
# https://git.archlinux.org/svntogit/community.git/tree/trunk/PKGBUILD?h=packages/splint
RUN cd /opt && \
    GIT_SSL_NO_VERIFY=true git clone http://repo.or.cz/splint-patched.git && \
    cd splint-patched && \
    $(automake --add-missing || true) && \
    $(autoreconf || true) && \
    automake --add-missing && \
    autoreconf && \
    ./configure --prefix=/usr --mandir=/usr/share/man && \
    make && \
    make install

# Export SaltyRTC test permanent key
ENV SALTYRTC_SERVER_PERMANENT_KEY=0919b266ce1855419e4066fc076b39855e728768e3afa773105edd2e37037c20
