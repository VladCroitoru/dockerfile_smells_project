FROM ubuntu:16.04

LABEL ubuntu.version="16.04" cutadapt.version="1.13" python.version="2.7.12" maintainer="Alice Minotto, @ Earlham Institute"

USER root

RUN apt-get -y update && apt-get -yy install python-pip && \
    pip install --upgrade cutadapt && \
    export PATH="$PATH:$HOME/.local/bin"

WORKDIR /data/
