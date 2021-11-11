FROM ubuntu:16.04 as builder
WORKDIR /src/github.com/calebcase/defcoin
RUN apt-get update && \
    apt-get install -y \
      build-essential \
      libssl-dev \
      libboost-all-dev \
      libdb++-dev \
      libminiupnpc-dev
COPY src src
COPY share share
RUN cd src && \
    make -j$(nproc) -f makefile.unix -e PIE=1

FROM ubuntu:16.04
RUN apt-get update && \
    apt-get install -y \
      libboost1.58 \
      libdb5.3++ \
      libminiupnpc10 \
      libssl1.0.0 \
      pwgen
COPY --from=builder /src/github.com/calebcase/defcoin/src/defcoind /bin/defcoind
COPY entrypoint /bin/entrypoint
EXPOSE 9337
ENTRYPOINT ["/bin/entrypoint"]
VOLUME ["/root/.defcoin"]
