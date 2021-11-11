FROM elixir:1.6.3
RUN \
    apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV MIX_ENV prod

COPY mix.* /usr/src/app/
RUN mix local.rebar
RUN mix local.hex --force
RUN mix deps.get

COPY . /usr/src/app

RUN mix compile

CMD mix server
