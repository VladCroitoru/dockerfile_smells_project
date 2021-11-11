FROM debian:jessie
MAINTAINER Adam Lindberg <hello@alind.io>

# Make apt-get happy
ENV DEBIAN_FRONTEND noninteractive
# Make Elixir happy
ENV LC_ALL C.UTF-8

# Install Erlang
RUN \
    # Add Erlang Solutions repository
    apt-get update && \
    apt-get install -y wget && \
    wget -qO- http://packages.erlang-solutions.com/debian/erlang_solutions.asc | apt-key add - && \
    echo "deb http://packages.erlang-solutions.com/debian jessie contrib" >> /etc/apt/sources.list && \
    apt-get purge -y wget && \
    apt-get autoremove -y && \
    # Install Erlang base
    apt-get update && \
    apt-get install -y erlang-base=1:18.0 && \
    # Clean up
    apt-get clean autoclean && \
    rm -rf /var/lib/apt/lists/*
