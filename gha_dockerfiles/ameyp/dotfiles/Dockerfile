# Adapted from
# https://github.com/michaelmior/dotfiles/blob/a9eae90d466958948a53b3b583d69eba844ed8f7/Dockerfile
FROM ubuntu:16.04

RUN apt-get update && \
    apt-get -y install \
        sudo \
 && apt-get clean

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN useradd -s /bin/bash tester
ADD . /home/tester/.dotfiles
RUN chown -R tester:tester /home/tester && \
    echo 'tester ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/tester && \
    chmod 0440 /etc/sudoers.d/tester
USER tester

ENV HOME /home/tester

WORKDIR /home/tester/.dotfiles
RUN ./install.sh