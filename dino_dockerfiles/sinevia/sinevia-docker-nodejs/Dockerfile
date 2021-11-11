FROM ubuntu:14.04
MAINTAINER Sinevia  <info@sinevia.com>
# Update OS
RUN apt-get update && apt-get upgrade -y

# Install SSHD
RUN apt-get install -qq openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed --in-place=.bak 's/without-password/yes/' /etc/ssh/sshd_config

# Install Node.js
RUN apt-get install python-software-properties python g++ make -y
RUN apt-get install software-properties-common wget unzip -y

RUN add-apt-repository ppa:chris-lea/node.js -y
RUN apt-get update
RUN apt-get install nodejs -y

RUN mkdir /site
ADD files/app.js /site/
ADD files/package.json /site/
ADD files/run_site.sh /

WORKDIR /site
RUN cd /site
RUN npm install

USER root
EXPOSE 80 22
CMD ["sh", "/run_site.sh"]
