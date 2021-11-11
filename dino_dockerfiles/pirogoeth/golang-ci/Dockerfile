FROM dock0/arch:latest
MAINTAINER Sean Johnson <sean.johnson@maio.me>

ENV GO_VERSION 1.7.3

RUN pacman -Syu --noconfirm
RUN pacman -S --noconfirm gcc

RUN curl https://raw.githubusercontent.com/travis-ci/gimme/master/gimme -o /usr/local/bin/gimme
RUN chmod +x /usr/local/bin/gimme

# Just to get the initial Go install set up.
RUN gimme ${GO_VERSION}
