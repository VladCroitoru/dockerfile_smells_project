FROM elixir:1.5

ADD . /app

WORKDIR /app

ENV MIX_ENV=prod
ENV PORT=8080

EXPOSE 8080

RUN mix local.hex --force
RUN mix local.rebar --force
RUN mix deps.get --only prod
RUN mix deps.get
RUN mix deps.compile
RUN mix compile
CMD mix phx.server
