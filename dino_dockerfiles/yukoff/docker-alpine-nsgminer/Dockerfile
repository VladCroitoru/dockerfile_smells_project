FROM alpine:latest
# for now VERSION is used to retrigger build, git checkouts to master
ENV VERSION ${VERSION:-0.9.3}
ENV HOME /nsgminer
COPY start.sh /nsgminer/
RUN adduser -S -D -H -h /nsgminer miner
RUN apk --no-cache upgrade && \
    apk --no-cache add \
      git \
      g++ \
      yasm \
      autoconf \
      automake \
      libtool \
      pkgconf \
      libcurl \
      curl-dev \
      gnutls-dev \
      uthash-dev \
      ncurses-libs \
      ncurses-dev \
      build-base && \
    git clone https://github.com/ghostlander/nsgminer.git /tmp/nsgminer && \
    cd /tmp/nsgminer && \
      ./autogen.sh --prefix=/nsgminer \
                   --enable-cpumining \
                   --enable-scrypt \
                   --enable-neoscrypt \
                   --disable-shared \
                   --enable-static && \
      make -j `grep -c ^processor /proc/cpuinfo` install && \
    cd /nsgminer && \
    rm -rf /tmp/*.patch /tmp/nsgminer && \
    apk del \
      build-base \
      ncurses-dev \
      uthash-dev \
      gnutls-dev \
      curl-dev \
      pkgconf \
      libtool \
      automake \
      autoconf \
      yasm \
      g++ \
      git
USER miner
WORKDIR /nsgminer
ENTRYPOINT ["/nsgminer/start.sh"]
#CMD ["-T", "--neoscrypt", "-o", "${POOL}", "-u", "${USER}", "-p", "${PASSWORD}"]
