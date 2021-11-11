FROM alpine:3.8 as builder

RUN apk --no-cache add ca-certificates git curl musl-dev gmp-dev zlib-dev pcre-dev ghc python
RUN apk --no-cache add --repository http://dl-cdn.alpinelinux.org/alpine/edge/community upx
RUN curl -sSL https://github.com/commercialhaskell/stack/releases/download/v1.6.5/stack-1.6.5-linux-x86_64-static.tar.gz | tar xvz && \
    mv stack*/stack /usr/bin

COPY stack.yaml /mnt
COPY *.cabal /mnt
WORKDIR /mnt
RUN rm -rf ~/.stack &&  \
    rm -rf ~/.ghc && \
    stack config set system-ghc --global true && \
    stack install --skip-ghc-check --split-objs --ghc-options="-fPIC -fllvm" --only-dependencies

COPY . /mnt

RUN echo '  ld-options: -static -Wl,--unresolved-symbols=ignore-all' >> crawler.cabal ; \
    stack install --split-objs --ghc-options="-fPIC -fllvm"
RUN upx --ultra-brute /root/.local/bin/crawler



FROM alpine:latest as runner

WORKDIR /root
COPY --from=builder /root/.local/bin/crawler .
RUN chmod +x ./crawler

CMD ["./crawler"]

