FROM bitwalker/alpine-elixir:1.12 as build
RUN mkdir /app
WORKDIR /app

COPY mix.exs mix.lock ./
RUN mix do deps.get, deps.compile

COPY . .
RUN export MIX_ENV=prod
CMD mix run --no-halt