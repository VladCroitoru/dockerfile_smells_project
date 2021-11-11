FROM ubuntu:16.04

LABEL ubuntu.version="16.04" cufflinks.version="2.2.1" maintainer="Alice Minotto, @ Earlham Institute"

USER root

RUN apt-get -y update && apt-get -yy install python \
    wget && \
    wget http://cole-trapnell-lab.github.io/cufflinks/assets/downloads/cufflinks-2.2.1.Linux_x86_64.tar.gz && \
    tar -zxvf cufflinks-2.2.1.Linux_x86_64.tar.gz && \
    rm cufflinks-2.2.1.Linux_x86_64.tar.gz && \
    mv cufflinks-2.2.1.Linux_x86_64/* bin/ && \
    rm -rf cufflinks-2.2.1.Linux_x86_64

WORKDIR /data/
