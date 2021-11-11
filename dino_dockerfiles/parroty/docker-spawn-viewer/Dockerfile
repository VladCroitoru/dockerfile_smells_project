FROM parroty/docker-elixir
MAINTAINER Parroty <xxxxxx@gmail.com>

## Prerequisites ##
RUN mix do local.rebar, local.hex --force

## Fetch the phoenix application ##
WORKDIR /usr/local/lib
RUN git clone https://github.com/parroty/spawn_viewer.git

## Compile ##
WORKDIR spawn_viewer
RUN mix do deps.get, compile

CMD ["mix", "run", "-e", "SpawnViewer.Router.start", "--no-deps-check", "--no-compile", "--no-halt"]

EXPOSE 4000
