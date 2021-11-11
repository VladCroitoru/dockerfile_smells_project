FROM ubuntu:latest

ENV ERLANG_VERSION 1:18.2
ENV ELIXIR_VERSION 1.2.3
ENV PHOENIX_VERSION 1.1.2

RUN apt-get update && apt-get upgrade -y && apt-get install -y openssl wget git make inotify-tools

# Elixir requires UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \
 && dpkg -i erlang-solutions_1.0_all.deb \
 && apt-get update \
 && apt-get install erlang=$ERLANG_VERSION -y \
 && apt-get install erlang-base-hipe=$ERLANG_VERSION -y \
 && rm erlang-solutions_1.0_all.deb

RUN git clone https://github.com/elixir-lang/elixir.git \
 && cd elixir \ 
 && git checkout v$ELIXIR_VERSION \
 && make

ENV PATH $PATH:/elixir/bin

# install Phoenix from source with some previous requirements
RUN git clone https://github.com/phoenixframework/phoenix.git \
 && cd phoenix && git checkout v$PHOENIX_VERSION \
 && mix local.hex --force && mix local.rebar --force \
 && mix do deps.get, compile \
 && wget https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez \
 && mix archive.install phoenix_new.ez --force

# install node/npm
RUN curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash -
RUN apt-get install -y nodejs


RUN apt-get -y install npm 
RUN npm install npm -g
RUN ln -s /usr/bin/nodejs /usr/bin/node

EXPOSE 4000

CMD ["/bin/bash"]