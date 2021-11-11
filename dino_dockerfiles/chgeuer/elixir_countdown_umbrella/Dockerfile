FROM alpine:3.7 as elixir

ENV ELIXIR_VERSION 1.5.2

RUN echo 'http://dl-4.alpinelinux.org/alpine/edge/main' >> /etc/apk/repositories && \
    apk --update add ncurses-libs wget curl git bash && \
    apk --update add nodejs nodejs-npm && \
    apk --update add erlang erlang-crypto erlang-syntax-tools erlang-parsetools \
                     erlang-inets erlang-ssl erlang-public-key erlang-eunit \
                     erlang-asn1 erlang-sasl erlang-erl-interface erlang-dev && \
    apk --update add --virtual build-dependencies ca-certificates && \
    wget --no-check-certificate "https://github.com/elixir-lang/elixir/releases/download/v${ELIXIR_VERSION}/Precompiled.zip" && \
    mkdir -p /opt/elixir-${ELIXIR_VERSION}/ && \
    unzip Precompiled.zip -d /opt/elixir-${ELIXIR_VERSION}/ && \
    rm Precompiled.zip && \
    apk del build-dependencies && \
    rm -rf /etc/ssl && \
    rm -rf /var/cache/apk/*

ENV PATH $PATH:/opt/elixir-${ELIXIR_VERSION}/bin

RUN mix local.hex --force && \
    mix local.rebar --force

CMD ["/bin/sh"]

##########################

FROM elixir as builder

WORKDIR /opt/app

COPY mix.exs mix.lock ./
COPY config config/
COPY . ./

ENV MIX_ENV=prod

RUN mix deps.get && \
    mix deps.compile && \
    cd apps/elixir_countdown_web/assets && \
    npm config set strict-ssl false && \
    npm install && \
    node node_modules/brunch/bin/brunch build && \
    cd ../../.. && \
    mix phx.digest && \
    mix release --env=$MIX_ENV

##########################

FROM alpine:3.7

ENV APP_NAME=elixir_countdown_umbrella \
    MIX_ENV=prod \
    PORT=4000

WORKDIR /

RUN echo 'http://dl-4.alpinelinux.org/alpine/edge/main' >> /etc/apk/repositories && \
    apk --update add ncurses-libs bash

COPY --from=builder /opt/app/_build/${MIX_ENV} /opt/app/_build/${MIX_ENV}

EXPOSE $PORT

ENTRYPOINT /opt/app/_build/${MIX_ENV}/rel/${APP_NAME}/bin/${APP_NAME} foreground
