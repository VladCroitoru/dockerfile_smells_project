FROM ubuntu:16.04

# upgrade the container
RUN apt-get update  && \
    apt-get upgrade -y

# install some prerequisites
RUN apt install -y git sudo && rm -rf /var/lib/apt/lists/*

# install torch
RUN git clone https://github.com/torch/distro.git /opt/torch --recursive
WORKDIR /opt/torch
# checkout to the 23/08/2017
RUN git checkout b6ea0652502cda80ccc174c47459ec1b0dc2a9c6
RUN bash install-deps
RUN ./install.sh

ENV PATH=/opt/torch/install/bin:$PATH