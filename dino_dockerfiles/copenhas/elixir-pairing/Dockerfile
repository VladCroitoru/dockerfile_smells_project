FROM copenhas/remote-pairing-container@latest

MAINTAINER Sean Copenhaver <sean.copenhaver@gmail.com>

RUN echo "deb http://packages.erlang-solutions.com/ubuntu trusty contrib" >> /etc/apt/sources.list && \
  wget http://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc && \
  sudo apt-key add erlang_solutions.asc && \
  sudo apt-get update && \
  sudo apt-get install -y \
    erlang \
    elixir

