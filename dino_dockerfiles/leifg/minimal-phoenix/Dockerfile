FROM shanesveller/elixir-lang:latest

MAINTAINER Leif Gensert <leif@gensert.de>

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update -q && \
    apt-get -y install apt-transport-https && \
    apt-get update -q && \
    apt-get clean -y && \
    rm -rf /var/cache/apt/*

ONBUILD WORKDIR /usr/src/app

ONBUILD ENV MIX_ENV prod
ONBUILD COPY mix.* /usr/src/app/
ONBUILD COPY config /usr/src/app/
ONBUILD RUN mix do deps.get, deps.compile
