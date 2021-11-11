FROM debian:stable

LABEL maintainer="jean-christophe.sirot@docker.com"

RUN apt-get update && apt-get install -y \
    curl \
    nmap \
    dnsutils \
    traceroute \
    tcpdump
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /usr/local/bin/
RUN rm -rf /var/lib/apt/lists/*
