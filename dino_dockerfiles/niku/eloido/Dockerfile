FROM elixir
MAINTAINER niku

ENV MIX_DEBUG=true \
    MIX_HOME=/root/.mix \
    MIX_ENV=prod

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN mix local.hex --force && \
    mix local.rebar --force && \
    mix deps.get && \
    mix compile

CMD ["mix", "run", "--no-halt"]
