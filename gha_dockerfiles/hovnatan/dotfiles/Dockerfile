FROM ubuntu:18.04
SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
	sudo git ca-certificates && \
  rm -rf /var/lib/apt/lists/*

COPY ./setup_on_docker.sh /root/
RUN /root/setup_on_docker.sh
