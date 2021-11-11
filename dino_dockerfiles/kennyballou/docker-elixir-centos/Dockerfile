# DOCKER-VERSION 1.9.1
FROM centos:7
MAINTAINER kballou@devnulllabs.io

ENV LANG="en_US.UTF-8"
ENV OTP_VER="19.0"
ENV REBAR_VERSION="2.6.1"
ENV REBAR3_VERSION="3.2.0"
ENV ELIXIR_VERSION="1.3.2"

RUN set -xe \
    && yum -y groupinstall "Development Tools" \
    && yum -y install ncurses \
        ncurses-devel \
        unixODBC \
        unixODBC-devel \
        openssl-devel \
    && OTP_SRC_URL="https://github.com/erlang/otp/archive/OTP-$OTP_VER.tar.gz" \
    && OTP_SRC_SUM="107b629aa7aea1bf76df0197629a50ce4fea61143ebb0e9a1b633b1fbaf9beb7" \
    && curl -fSL "$OTP_SRC_URL" -o otp-src.tar.gz \
    && echo "${OTP_SRC_SUM}  otp-src.tar.gz" | sha256sum -c - \
    && mkdir -p /usr/src/otp-src \
    && tar -zxf otp-src.tar.gz -C /usr/src/otp-src --strip-components=1 \
    && rm otp-src.tar.gz \
    && cd /usr/src/otp-src \
    && ./otp_build autoconf \
    && ./configure \
    && make \
    && make install \
    && find /usr/local -name examples | xargs rm -rf \
    && cd /usr/src \
    && rm -rf /usr/src/otp-src \
    && REBAR_SRC_URL="https://github.com/rebar/rebar/archive/${REBAR_VERSION##*@}.tar.gz" \
    && REBAR_SRC_SUM="aed933d4e60c4f11e0771ccdb4434cccdb9a71cf8b1363d17aaf863988b3ff60" \
    && mkdir -p /usr/src/rebar-src \
    && curl -fSL "$REBAR_SRC_URL" -o rebar-src.tar.gz \
    && echo "${REBAR_SRC_SUM}  rebar-src.tar.gz" | sha256sum -c - \
    && tar -zxf rebar-src.tar.gz -C /usr/src/rebar-src --strip-components=1 \
    && rm rebar-src.tar.gz \
    && cd /usr/src/rebar-src \
    && ./bootstrap \
    && install -v ./rebar /usr/local/bin \
    && cd /usr/src \
    && rm -rf /usr/src/rebar-src \
    && REBAR3_SRC_URL="https://github.com/erlang/rebar3/archive/${REBAR3_VERSION##*@}.tar.gz" \
    && REBAR3_SRC_SUM="78ad27372eea6e215790e161ae46f451c107a58a019cc7fb4551487903516455" \
    && mkdir -p /usr/src/rebar3-src \
    && curl -fSL "$REBAR3_SRC_URL" -o rebar3-src.tar.gz \
    && echo "${REBAR3_SRC_SUM}  rebar3-src.tar.gz" | sha256sum -c - \
    && tar -zxf rebar3-src.tar.gz -C /usr/src/rebar3-src --strip-components=1 \
    && rm rebar3-src.tar.gz \
    && cd /usr/src/rebar3-src \
    && HOME=$PWD ./bootstrap \
    && install -v ./rebar3 /usr/local/bin \
    && cd /usr/src \
    && rm -rf /usr/src/rebar3-src \
    && ELIXIR_SRC_URL="https://github.com/elixir-lang/elixir/archive/v$ELIXIR_VERSION.tar.gz" \
    && ELIXIR_SRC_SUM="be24efee0655206063208c5bb4157638310ff7e063b7ebd9d79e1c77e8344c4b" \
    && curl -fSL "$ELIXIR_SRC_URL" -o elixir.tar.gz \
    && echo "${ELIXIR_SRC_SUM}  elixir.tar.gz" | sha256sum -c - \
    && mkdir -p /usr/src/elixir-src \
    && tar -zxf elixir.tar.gz -C /usr/src/elixir-src --strip-components=1 \
    && rm -f elixir.tar.gz \
    && cd /usr/src/elixir-src \
    && make install \
    && cd / \
    && rm -rf /usr/src/elixir-src \
    && mix local.hex --force \
    && mix hex.info
