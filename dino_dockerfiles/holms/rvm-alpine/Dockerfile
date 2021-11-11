FROM alpine:3.8

# Install bash
RUN apk update && apk add bash && rm -rf /var/cache/apk/*
RUN /bin/bash
RUN apk update \
  && apk add alpine-sdk gcc gnupg curl ruby procps musl-dev make linux-headers \
        zlib zlib-dev openssl openssl-dev libssl1.0 shadow \
  && curl -sSL https://github.com/rvm/rvm/tarball/stable -o rvm-stable.tar.gz \
  && echo 'export rvm_prefix="$HOME"' > /root/.rvmrc \
  && echo 'export rvm_path="$HOME/.rvm"' >> /root/.rvmrc \
  && mkdir rvm && cd rvm \
  && tar --strip-components=1 -xzf ../rvm-stable.tar.gz \
  && ./install --auto-dotfiles --autolibs=0 \
  && cd ../ && rm -rf rvm-stable stable.tar.gz rvm \ 
  && apk del alpine-sdk gcc gnupg musl-dev make linux-headers zlib-dev openssl-dev musl-dev \
  && rm -rf /var/cache/apk/*

RUN source ~/.rvm/scripts/rvm
