FROM rijalati/alpine-java8
MAINTAINER rijalati@gmail.com

RUN git clone https://github.com/rijalati/oltpbench.git
WORKDIR /oltpbench

RUN ant
WORKDIR /
RUN git clone https://github.com/rijalati/dotfiles.git \
    && cp /dotfiles/mkshrc /root/.mkshrc
WORKDIR /oltpbench
RUN mkdir /oltpbench/templates
COPY templates/ templates/
RUN sed 's|#!/bin/bash|#!/bin/sh|' oltpbenchmark > mod.oltpbenchmark \
    && mv mod.oltpbenchmark oltpbenchmark \
    && chmod +x oltpbenchmark
ENTRYPOINT ["/oltpbench/oltpbenchmark"]
CMD ["--help"]
