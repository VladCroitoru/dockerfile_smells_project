FROM ubuntu:14.04
MAINTAINER asiainfo

# Set locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install base package
RUN apt-get update
RUN apt-get install -y wget git build-essential

# Install Elixir
RUN wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
RUN dpkg -i erlang-solutions_1.0_all.deb
RUN apt-get update
RUN apt-get install -y erlang erlang-inets erlang-ssl elixir

# Install Phoenix and run tests.
WORKDIR /opt
RUN git clone https://github.com/phoenixframework/phoenix.git
WORKDIR /opt/phoenix
RUN mix local.rebar --force
RUN mix local.hex --force
RUN git checkout v0.7.2 && mix do deps.get, compile
RUN mix test
