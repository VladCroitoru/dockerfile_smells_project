FROM ubuntu:latest

MAINTAINER Mateo R, <mateoradic16@gmail.com>

RUN apt update && \
    apt -y install tzdata && \
    apt -y install lib32gcc1 screen wget && \
    useradd -d /home/container -m container

USER container
ENV  USER container
ENV  HOME /home/container

WORKDIR /home/container

COPY ./entrypoint.sh /entrypoint.sh

CMD ["/bin/bash", "/entrypoint.sh"]
