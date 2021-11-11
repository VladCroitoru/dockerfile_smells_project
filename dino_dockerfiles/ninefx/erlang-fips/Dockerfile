FROM ninefx/alpine-fips:3.6

ARG OTP_VERSION=20.3.4
ARG OTP_SHA256_HASH=6a3b8d42b49dde708ab6faea4bf56b12466d0435e95314f42cedc0471ffcf7ae

COPY check_fips/ /root/check_fips/

ENV PATH "$PATH:/root/.cache/rebar3/bin/"

RUN apk update \
    && apk upgrade \
    && apk add wget ca-certificates gcc gzip tar libc-dev ca-certificates make coreutils autoconf ncurses-dev unixodbc \
    && cd /root \
    && wget --quiet https://github.com/erlang/otp/archive/OTP-$OTP_VERSION.tar.gz \
    && openssl dgst -sha256 OTP-$OTP_VERSION.tar.gz | grep $OTP_SHA256_HASH \
    && tar xfz OTP-$OTP_VERSION.tar.gz \
    && rm OTP-$OTP_VERSION.tar.gz \
    && cd otp-OTP-$OTP_VERSION \
    && export ERL_TOP=`pwd` \
    && ./otp_build autoconf \
    && ./configure --enable-fips \
    && make \
    && make install \
    && wget https://s3.amazonaws.com/rebar3/rebar3 \
    && chmod +x rebar3 \
    && ./rebar3 local install \
    && ./rebar3 local upgrade \
    && cd /root/check_fips/ \
    && rebar3 escriptize \
    && chmod u+x _build/default/bin/check_fips \
    && ./_build/default/bin/check_fips \
    && cd /root \
    && rm -rf .ash_history .wget-hsts otp-OTP-$OTP_VERSION check_fips rebar3 \
    && apk --purge del wget ca-certificates gcc gzip tar libc-dev ca-certificates make coreutils autoconf ncurses-dev
