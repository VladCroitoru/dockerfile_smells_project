FROM elixir:latest
RUN apt-get update
ENV PORT 4040
RUN mkdir /wmart
WORKDIR /wmart
ADD mix.exs /wmart/mix.exs
ADD mix.lock /wmart/mix.lock
RUN mix local.hex --force
RUN mix local.rebar --force
RUN mix deps.get
ADD . /wmart
