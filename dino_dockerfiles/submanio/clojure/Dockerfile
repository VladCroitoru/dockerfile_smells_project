FROM ubuntu:14.04
MAINTAINER Vladimir Iakovlev <nvbn.rm@gmail.com>

ENV CLOJURE_UPDATED "201529032119"
RUN adduser --disabled-password --gecos "" clojure

RUN apt-get update -yqq
RUN apt-get upgrade -yqq
RUN apt-get install openjdk-7-jdk curl git -yqq --no-install-recommends
RUN curl -s https://raw.githubusercontent.com/technomancy/leiningen/2.5.0/bin/lein > /usr/local/bin/lein
RUN chmod 0755 /usr/local/bin/lein

WORKDIR /home/clojure
USER clojure
RUN lein version
USER root

ONBUILD COPY . /home/clojure/code
ONBUILD RUN chown -R clojure code
ONBUILD WORKDIR /home/clojure/code
ONBUILD USER clojure
ONBUILD RUN lein deps
