FROM ubuntu:16.04

MAINTAINER Nobutaka SAITO <nobutaka.saitoh@gmail.com>

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y gcc make bzip2 libssl-dev libreadline-dev zlib1g-dev wget git firefox
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.20.0/geckodriver-v0.20.0-linux64.tar.gz && \
    tar -zxf geckodriver-v0.20.0-linux64.tar.gz && \
    mv geckodriver /usr/local/bin
RUN git clone https://github.com/rbenv/rbenv.git      ~/.rbenv && \
    git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build && \
    echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc && \
    echo 'eval "$(rbenv init -)"' >> ~/.bashrc

ENV PATH ~/.rbenv/bin:$PATH

RUN eval "$(rbenv init -)" && \
    rbenv install 2.5.0 && \
    rbenv global 2.5.0 && \
    rbenv rehash && \
    gem install selenium-webdriver

COPY tests /tests

COPY entrypoint.sh /
ENTRYPOINT [ "/entrypoint.sh" ]
