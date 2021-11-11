FROM elixir:alpine

RUN apk --update --no-cache add \
  nodejs-npm \
  make \
  g++ \
  inotify-tools

RUN mkdir /app
WORKDIR /app

COPY assets/ /app/assets/
COPY lib/ /app/lib/
COPY config/ /app/config/
COPY priv/ /app/priv/
COPY test/ /app/test/
COPY mix.* /app/
COPY README.md /app/README.md

RUN mix local.hex --force
RUN mix deps.get
RUN mix local.rebar
RUN mix deps.compile

RUN cd assets && \
  npm install && \
  node node_modules/brunch/bin/brunch build

CMD ["mix", "phx.server"]
