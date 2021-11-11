FROM alpine:3.8

ENV ELIXIR_VERSION "1.8.1-otp-21"
ENV ERLANG_VERSION "21.0"
ENV ASDF_VERSION   "v0.5.1"

RUN apk add --no-cache autoconf bash curl alpine-sdk perl openssl openssh-client openssl-dev ncurses ncurses-dev unixodbc unixodbc-dev python py-pip py-setuptools git ca-certificates nodejs libxslt libxml2-utils && \
    export PATH="$HOME/.asdf/bin:$HOME/.asdf/shims:$PATH" && \
    echo "PATH=$HOME/.asdf/bin:$HOME/.asdf/shims:$PATH" >> /root/.profile && \
    git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch $ASDF_VERSION && \
    asdf plugin-add erlang https://github.com/asdf-vm/asdf-erlang.git && \
    asdf install erlang $ERLANG_VERSION && \
    asdf global  erlang $ERLANG_VERSION && \
    asdf plugin-add elixir https://github.com/asdf-vm/asdf-elixir.git && \
    asdf install elixir $ELIXIR_VERSION && \
    asdf global  elixir $ELIXIR_VERSION && \
    yes | mix local.hex --force && \
    yes | mix local.rebar --force && \
    pip install --no-cache-dir python-dateutil && \
    git clone https://github.com/s3tools/s3cmd.git /opt/s3cmd && \
    ln -s /opt/s3cmd/s3cmd /usr/bin/s3cmd

ENTRYPOINT sh --login
