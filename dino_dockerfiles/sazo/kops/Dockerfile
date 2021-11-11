FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -y wget curl awscli vim \
    && wget -O /usr/bin/kops https://github.com/kubernetes/kops/releases/download/v1.4.4/kops-linux-amd64 \
    && chmod +x /usr/bin/kops \
    && wget -P /usr/local/bin/ https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl \
    && chmod +x /usr/local/bin/kubectl