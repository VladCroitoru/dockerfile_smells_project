FROM ubuntu:17.10

RUN \
    apt-get update && \
    apt-get upgrade && \
    apt-get install -y wget && \
    apt-get install -y curl

RUN \
    wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && \
    dpkg -i erlang-solutions_1.0_all.deb

RUN \
    apt-get update && \
    apt-get install -y erlang

RUN \
    curl https://s3.amazonaws.com/rebar3/rebar3 -o /usr/bin/rebar3 && \
    chmod +x /usr/bin/rebar3
