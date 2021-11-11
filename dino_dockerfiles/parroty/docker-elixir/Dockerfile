FROM ubuntu:14.04
MAINTAINER Parroty <xxxxxx@gmail.com>

# Install base package
RUN apt-get update
RUN apt-get install -y wget git build-essential

# Install Erlang
RUN wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
RUN dpkg -i erlang-solutions_1.0_all.deb
RUN apt-get update
RUN apt-get install -y erlang

# Install Elixir
WORKDIR /tmp/elixir-build
RUN git clone https://github.com/elixir-lang/elixir.git
WORKDIR elixir
RUN git checkout v0.14.2 && make && make install
