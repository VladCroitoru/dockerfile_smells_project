FROM ubuntu:latest
MAINTAINER Martin Souchal "souchal@apc.in2p3.fr"

RUN apt-get update && \
    apt-get install -y wget software-properties-common build-essential sgml-base rsync xml-core openssh-client && \
    apt-get clean

RUN add-apt-repository universe && \
    apt-get update && \
    apt-get -y install cmake git gfortran openmpi-common openmpi-bin libopenmpi-dev && \
    apt-get clean

RUN mkdir /data

ENTRYPOINT echo "Le runscript est la commande par défaut du conteneur !"

ADD ./mpi-ping.c /data/mpi-ping.c
