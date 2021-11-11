FROM ubuntu:rolling

RUN apt-get update && apt-get install -y \
    texlive-full \
    xindy \
    openjdk-8-jre \
    cm-super \
    git \
    librsvg2-bin \
    graphviz \
&& rm -rf /var/lib/apt/lists/*
