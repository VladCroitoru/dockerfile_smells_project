FROM phusion/baseimage:latest
MAINTAINER Berend Weel <b.weel@esciencecenter.nl>

# Keep ssh running
RUN rm -f /etc/service/sshd/down
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

RUN apt-get update && apt-get install -y nodejs nodejs-legacy npm git libsass-dev

RUN npm i -g npm
RUN npm i -g n
RUN n latest
RUN npm i -g typescript@1.8.10 bower nodemon http-server gulp node-gyp@3.4.0 js-beautify@1.5.10 typings@1.3.3

RUN /usr/sbin/useradd -p $(openssl passwd simcity) -d /home/simcity -m --shell /bin/bash simcity

WORKDIR /home/simcity/
COPY . csWeb/
RUN chown simcity:simcity -R /home/simcity

USER simcity
RUN mkdir ~/npm && echo "prefix = ~/npm" > ~/.npmrc && echo "export PATH=~/npm/bin:$PATH" >> ~/.profile && . ~/.profile

WORKDIR /home/simcity/csWeb
RUN npm install
RUN bower install
RUN gulp init
RUN bower link

WORKDIR /home/simcity/csWeb/out/csServerComp
RUN npm link

USER root
CMD ["/sbin/my_init"]
