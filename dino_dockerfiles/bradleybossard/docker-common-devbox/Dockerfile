FROM ubuntu:16.04
MAINTAINER Bradley Bossard <bradleybossard@gmail.com>

# Build the image
# docker build --rm -t docker-common-devbox .

# Fire up an instance with a bash shell
# docker run --rm -i -t docker-common-devbox

# Replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# make sure apt is up to date
RUN apt-get update --fix-missing && \
    apt-get remove ack && \
    apt-get install -y git \
                       git-extras \
                       tig \
                       curl \
                       wget \
                       tmux \
                       vim \
                       grc \
                       tree \
                       ack-grep

# RUN dpkg-divert --local --divert /usr/bin/ack --rename --add /usr/bin/ack-grep                       

WORKDIR /root
RUN git clone https://github.com/bradleybossard/dotfiles.git
RUN git clone https://github.com/gmarik/vundle.git ./.vim/bundle/vundle
RUN cd dotfiles; sh setup.sh;

ENV TERM xterm

