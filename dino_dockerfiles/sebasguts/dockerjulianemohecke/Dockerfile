## Dockerfile for the DFG SPP Computeralgebra Software

FROM ubuntu:utopic

MAINTAINER Sebastian Gutsche <sebastian.gutsche@gmail.com>

RUN apt-get update -qq \
    && adduser --quiet --shell /bin/bash --gecos "spp user,101,," --disabled-password spp \
    && adduser spp sudo \
    && chown -R spp:spp /home/spp/ \
    && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER spp

# # Nemo
RUN    sudo apt-get install -y software-properties-common \
    && sudo apt-add-repository ppa:staticfloat/julianightlies \
    && sudo apt-add-repository ppa:staticfloat/julia-deps \
    && sudo apt-get -qq update \
    && sudo apt-get install -y julia wget vim g++ git build-essential \
    && cd /tmp \
    && touch nemo_install \
    && echo 'Pkg.clone("https://github.com/fieker/Nemo.jl")' > nemo_install \
    && echo 'Pkg.clone("https://github.com/thofma/hecke")' >> nemo_install \
    && echo 'Pkg.build("Nemo")' >> nemo_install \
    && julia nemo_install \
    && rm nemo_install

ENV HOME /home/spp
ENV PATH /home/spp/bin:$PATH
WORKDIR /home/spp

