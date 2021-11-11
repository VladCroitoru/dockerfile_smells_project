FROM ubuntu:20.04

RUN apt-get update

RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq locales
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en  LC_ALL=en_US.UTF-8

RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq openjdk-11-jdk
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq curl make
RUN cd /tmp && \
  curl -O https://download.clojure.org/install/linux-install-1.10.3.855.sh && \
  chmod +x linux-install-1.10.3.855.sh && \
  bash ./linux-install-1.10.3.855.sh

RUN mkdir /task
WORKDIR /task

COPY deps.edn /task/
RUN echo '(+ 1 1)' | clojure
COPY Makefile worker.sh /task/
COPY src /task/src
