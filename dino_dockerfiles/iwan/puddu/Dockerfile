FROM elixir:1.6.1-alpine
MAINTAINER Iwan Buetti <iwan.buetti@gmail.com>

RUN mix local.hex --force

RUN mix archive.install https://github.com/phoenixframework/archives/raw/master/phx_new.ez --force
RUN apk add --update nodejs inotify-tools && rm -rf /var/cache/apk/*

RUN mkdir /app
COPY . /app
WORKDIR /app

ENV MIX_ENV=prod
ENV PORT=4000

RUN mix local.rebar --force
RUN mix deps.get --only prod
RUN mix compile

WORKDIR /app/assets
RUN npm install
RUN node node_modules/brunch/bin/brunch build --production

WORKDIR /app
RUN mix phx.digest
