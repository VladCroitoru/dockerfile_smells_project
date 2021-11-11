FROM ubuntu:16.04

LABEL ubuntu.version="16.04" muscle.version="3.8.31" maintainer="Alice Minotto, @ Earlham Institute"

USER root

RUN apt-get -y update && apt-get -yy install muscle

WORKDIR /data/
