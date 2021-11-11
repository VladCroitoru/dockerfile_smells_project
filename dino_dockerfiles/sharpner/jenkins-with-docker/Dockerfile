FROM jenkins:latest

USER root

RUN curl -sSL https://get.docker.com/ | sh
RUN curl -sL https://deb.nodesource.com/setup | bash -

RUN apt-get install -y build-essential make nodejs

USER jenkins

