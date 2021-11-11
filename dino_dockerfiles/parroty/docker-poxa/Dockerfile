FROM parroty/docker-elixir
MAINTAINER parroty <xxxxxx@gmail.com>

## Prerequisites ##
RUN mix do local.rebar, local.hex --force

## Fetch the phoenix application ##
WORKDIR /usr/local/lib
RUN git clone https://github.com/edgurgel/poxa.git

## Compile ##
WORKDIR poxa
RUN mix do deps.get, compile

CMD ["mix", "run", "--no-halt"]

EXPOSE 8080
