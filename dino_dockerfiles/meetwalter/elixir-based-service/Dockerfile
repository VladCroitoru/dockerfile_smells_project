FROM elixir:1.4

ENV MIX_ENV=prod

EXPOSE 2022

ENTRYPOINT ["/usr/local/bin/docker-entrypoint"]
CMD ["start"]


RUN mix do local.hex --force, local.rebar --force

COPY ./bin /usr/local/bin
COPY ./node /node
WORKDIR /node/apps/scaffold

RUN mix do deps.get, deps.compile, compile
