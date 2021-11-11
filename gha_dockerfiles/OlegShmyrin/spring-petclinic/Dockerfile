FROM maven:3.6.3-openjdk-17-slim

RUN useradd -m -u 1000 -s /bin/bash jenkins
RUN apt-get clean
RUN apt-get update
RUN apt install -y openssh-client
