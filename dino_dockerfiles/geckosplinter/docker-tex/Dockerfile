FROM ubuntu:latest
MAINTAINER Gecko Splinter gecko.splinter@gmail.com

RUN apt-get -qq update && apt-get install -y -q \
    texlive-full \
    latex-beamer \
    context \
    pandoc \
    make \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/*

WORKDIR /data
VOLUME ["/data"]

CMD ["/bin/bash"]
