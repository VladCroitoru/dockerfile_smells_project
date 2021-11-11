FROM ubuntu:yakkety

RUN apt-get update \
    && apt-get install -y build-essential patch ruby-dev zlib1g-dev liblzma-dev git \
    && gem install git_stats \
    && apt-get clean
