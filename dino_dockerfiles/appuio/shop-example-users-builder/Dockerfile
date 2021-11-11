# extend alpine
FROM alpine:3.5

# specify the elixir version
ENV ELIXIR_VERSION 1.4.2
ENV MIX_ENV prod
ENV PORT 4000

# install erlang and elixir
RUN apk --update add --no-cache --virtual .build-deps wget ca-certificates && \
    apk add --no-cache \
      make \
      g++ \
      erlang \
      erlang-crypto \
      erlang-syntax-tools \
      erlang-parsetools \
      erlang-inets \
      erlang-ssl \
      erlang-public-key \
      erlang-eunit \
      erlang-asn1 \
      erlang-sasl \
      erlang-erl-interface \
      erlang-dev && \
    wget --no-check-certificate https://github.com/elixir-lang/elixir/releases/download/v${ELIXIR_VERSION}/Precompiled.zip && \
    mkdir -p /opt/elixir-${ELIXIR_VERSION}/ && \
    unzip Precompiled.zip -d /opt/elixir-${ELIXIR_VERSION}/ && \
    rm Precompiled.zip && \
    apk del .build-deps

# add the elixir installation to path
ENV PATH $PATH:/opt/elixir-${ELIXIR_VERSION}/bin

# initialize hex and rebar
RUN erl && \
    mix local.hex --force && \
    mix local.rebar --force

# add a new dir for the app
RUN mkdir -p /app/source
WORKDIR /app/source

# run shell as default command
CMD ["/bin/sh"]
