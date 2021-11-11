FROM elixir:1.5.2-alpine

RUN apk update && apk add git

ENV MIX_ENV prod

RUN mix local.hex --force
RUN mix local.rebar --force

COPY mix.* ./

RUN mix deps.get --only prod
RUN mix deps.compile

COPY . .

RUN mix compile
RUN mix escript.build

CMD ./base16_builder
