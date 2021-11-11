FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  git wget curl && \
  rm -Rf /var/lib/apt/lists && rm -Rf /var/cache/apt/archives

RUN cd /tmp; wget -q -O docker.tgz https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz && \
  tar -zxf docker.tgz && \
  mv docker/docker /usr/bin/docker && \
  rm -Rf docker.tgz docker
