FROM ubuntu:latest
RUN mkdir -p ~/.ssh
RUN echo "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config
RUN apt-get update \
        && apt-get install -y openssh-client \
        && rm -rf /var/lib/apt/lists/*
