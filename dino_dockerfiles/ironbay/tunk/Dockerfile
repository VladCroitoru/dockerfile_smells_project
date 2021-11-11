FROM elixir:1.8.1-alpine

RUN apk add --no-cache git
RUN apk add --no-cache alpine-sdk

RUN yes | mix local.hex
RUN yes | mix local.rebar

ENV MIX_ENV=prod

WORKDIR /tmp
ADD mix.exs mix.exs
ADD mix.lock mix.lock
ADD config config
RUN mix deps.clean --all
RUN mix deps.get
RUN mix deps.compile

WORKDIR /app
ADD . .
RUN cp -a /tmp/deps .
RUN cp -a /tmp/_build .
RUN ls -lah
RUN mix release

CMD mix run --no-halt
