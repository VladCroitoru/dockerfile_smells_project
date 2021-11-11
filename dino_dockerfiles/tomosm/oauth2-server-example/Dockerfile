FROM node:latest

RUN apt-get update
RUN apt-get install -y ocaml libelf-dev git

RUN useradd -d /home/oauth2 -m oauth2 && echo 'oauth2 ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER oauth2
RUN echo 'export LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"' >> ~/.bashrc

RUN git clone https://github.com/tomosm/oauth2-server-example.git ~/oauth2-server

RUN cd /home/oauth2/oauth2-server && git submodule init && git submodule update && npm install
WORKDIR /home/oauth2/oauth2-server

EXPOSE 3000
