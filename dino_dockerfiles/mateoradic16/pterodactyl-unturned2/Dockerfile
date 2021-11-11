FROM ubuntu:latest

MAINTAINER Mateo R, <mateoradic16@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN dpkg --add-architecture amd64 && \
    apt update && \
    apt upgrade -y && \
    apt install -y curl screen htop unzip build-essential gcc-multilib rpm libstdc++6:amd64 libgcc1:amd64 zlib1g:amd64 libncurses5:amd64 mono-reference-assemblies-2.0 mono-devel libmono-cil-dev mono-runtime libc6:amd64 libgl1-mesa-glx:amd64 libxcursor1:amd64 libxrandr2:amd64 && \
    useradd -d /home/container -m container

USER container
ENV  USER container
ENV  HOME /home/container

WORKDIR /home/container

COPY ./entrypoint.sh /entrypoint.sh

CMD ["/bin/bash", "/entrypoint.sh"]
