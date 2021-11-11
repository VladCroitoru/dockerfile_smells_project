FROM ubuntu:latest

MAINTAINER Isaac A, <isaac@isaacs.site>

ENV DEBIAN_FRONTEND noninteractive

RUN dpkg --add-architecture i386 && \
    apt update && \
    apt upgrade -y && \
    apt install -y curl screen htop unzip lib32stdc++6 mono-runtime mono-reference-assemblies-2.0 libc6:i386 libgl1-mesa-glx:i386 libxcursor1:i386 libxrandr2:i386 libc6-dev-i386 libgcc-4.8-dev:i386 && \
    useradd -d /home/container -m container

USER container
ENV  USER container
ENV  HOME /home/container

WORKDIR /home/container

COPY ./entrypoint.sh /entrypoint.sh

CMD ["/bin/bash", "/entrypoint.sh"]
