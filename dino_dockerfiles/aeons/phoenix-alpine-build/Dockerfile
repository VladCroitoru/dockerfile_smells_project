FROM alpine:3.5
MAINTAINER Bjørn Madsen <bm@aeons.dk>

ENV REFRESHED_AT 2017-03-15
ENV ASDF_VERSION v0.2.1
ENV ERLANG_VERSION 19.3
ENV ELIXIR_VERSION 1.4.2
ENV YARN_VERSION 0.22.0

RUN apk add --no-cache bash alpine-sdk nodejs ncurses-dev libressl-dev perl && \
    export PATH="$HOME/.asdf/bin:$HOME/.asdf/shims:$PATH" && \
    echo "PATH=$HOME/.asdf/bin:$HOME/.asdf/shims:$PATH" >> ~/.profile && \
    git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch $ASDF_VERSION && \
    asdf plugin-add erlang https://github.com/asdf-vm/asdf-erlang.git && \
    asdf install erlang $ERLANG_VERSION && \
    asdf global erlang $ERLANG_VERSION && \
    asdf plugin-add elixir https://github.com/asdf-vm/asdf-elixir.git && \
    asdf install elixir $ELIXIR_VERSION && \
    asdf global elixir $ELIXIR_VERSION && \
    mix local.hex --force && \
    mix local.rebar --force && \
    curl -o- -L https://yarnpkg.com/install.sh | bash -s -- --version $YARN_VERSION

SHELL ["/bin/bash", "-lc"]
