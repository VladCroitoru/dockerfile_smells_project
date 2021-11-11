FROM docker:rc-git

# Install erlang
ARG ERLANG_VERSION=20.0

ARG DISABLED_APPS='megaco wx debugger jinterface orber reltool observer gs et'
ARG ERLANG_DOWNLOAD_URL="https://github.com/erlang/otp/archive/OTP-${ERLANG_VERSION}.tar.gz"

RUN set -xe \
    && apk --update --no-cache add build-base openssl ca-certificates ncurses-libs ncurses \
    && rm -rf \
      /var/cache/apk/* \
      /tmp/*
    
RUN set -xe \
    && apk --update add --virtual build-dependencies curl ca-certificates autoconf perl ncurses-dev openssl-dev unixodbc-dev tar unixodbc \
    && curl -fSL -o otp-src.tar.gz "$ERLANG_DOWNLOAD_URL" \
    && mkdir -p /usr/src/otp-src \
    && tar -xzf otp-src.tar.gz -C /usr/src/otp-src --strip-components=1 \
    && rm otp-src.tar.gz \
    && cd /usr/src/otp-src \
    && for lib in ${DISABLED_APPS} ; do touch lib/${lib}/SKIP ; done \
    && ./otp_build autoconf \
    && ./configure \
        --enable-smp-support \
        --enable-m64-build \
        --disable-native-libs \
        --enable-sctp \
        --enable-threads \
        --enable-kernel-poll \
        --disable-hipe \
    && make -j$(getconf _NPROCESSORS_ONLN) \
    && make install \
    && find /usr/local -name examples | xargs rm -rf \
    && apk del build-dependencies \
    && ls -d /usr/local/lib/erlang/lib/*/src | xargs rm -rf \
    && rm -rf \
      /opt \
      /var/cache/apk/* \
      /tmp/* \
      /usr/src

ARG ELIXIR_VERSION=1.5.0

RUN set -xe \
    && apk --update add --virtual build-dependencies wget ncurses-libs ca-certificates \
    && wget --no-check-certificate https://github.com/elixir-lang/elixir/releases/download/v${ELIXIR_VERSION}/Precompiled.zip \
    && mkdir -p /opt/elixir-${ELIXIR_VERSION}/ \
    && unzip Precompiled.zip -d /opt/elixir-${ELIXIR_VERSION}/ \
    && rm Precompiled.zip \
    && apk del build-dependencies \
    && rm -rf /etc/ssl \
    && rm -rf \
      /var/cache/apk/* \
      /tmp/*

ENV PATH $PATH:/opt/elixir-${ELIXIR_VERSION}/bin


# Install hex
RUN mix local.hex --force \
    && mix local.rebar --force

RUN git config --system http.sslverify false && \
  git clone https://github.com/tagip/hex.git && \
  cd hex && \
  mix deps.get && \
  mix install

CMD ["/bin/sh"]
