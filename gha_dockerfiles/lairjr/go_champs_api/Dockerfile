FROM elixir:latest

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN mix local.hex --force
RUN mix local.rebar --force
RUN mix deps.get

RUN mix do compile

CMD ["/app/entrypoint.sh"]