FROM alpine:edge as builder

RUN apk add autoconf libtool automake git bash perl boost-dev build-base linux-headers openssl-dev libevent-dev

RUN git clone https://github.com/GarlicoinOrg/Garlicoin.git

RUN cd /Garlicoin \
  && ./autogen.sh \
  && ./configure --disable-wallet --disable-tests \
  && make -j 8 \
  && make install

FROM alpine:edge

COPY --from=builder /usr/local/bin/garlicoin-cli /usr/local/bin/garlicoin-cli
COPY --from=builder /usr/local/bin/garlicoin-tx /usr/local/bin/garlicoin-tx
COPY --from=builder /usr/local/bin/garlicoind /usr/local/bin/garlicoind

RUN apk add --no-cache openssl libevent boost boost-program_options

EXPOSE 42070

ENTRYPOINT ["/usr/local/bin/garlicoind", "-server", "-disablewallet", "-printtoconsole"]

CMD ["-txindex", "-rpcworkqueue=32", "-rpcuser=user", "-rpcpassword=pass"]