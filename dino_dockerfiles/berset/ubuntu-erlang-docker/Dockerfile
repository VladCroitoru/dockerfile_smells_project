FROM ubuntu:16.04

RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y --no-install-recommends wget build-essential git ca-certificates && \
  wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && \
  dpkg -i erlang-solutions_1.0_all.deb && \
  apt-get update && \
  apt-get install -y --no-install-recommends erlang-nox erlang-dev erlang-src
COPY rebar /usr/local/bin/rebar
COPY validate_config /usr/local/bin/validate_config

