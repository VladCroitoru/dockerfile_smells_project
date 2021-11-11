FROM msaraiva/elixir-dev:1.2.2

ADD . /app

WORKDIR /app

RUN mix local.hex && mix hex.info && mix deps.get && mix deps.compile && mix compile

CMD ["mix", "run", "--no-halt"]
