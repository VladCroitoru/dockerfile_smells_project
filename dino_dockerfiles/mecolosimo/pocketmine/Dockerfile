FROM ubuntu:latest
MAINTAINER Marc Colosimo <enzo69mc@gmail.com>

RUN apt-get update -y; apt-get upgrade -y
RUN apt-get install -y python3-yaml python-setuptools 
RUN apt-get install -y supervisor openssh-server curl rsync
RUN easy_install pip && pip install superlance

# set up ssh
# either copy your pubkey to root's .ssh/authorized_keys or this
RUN mkdir /var/run/sshd
RUN sed -i 's/^PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN echo 'root:root' | chpasswd

# set up supervisor
ADD ./src/etc/supervisor /etc/supervisor

# Supervisord's http port (configured)
EXPOSE 9001

# make local pocketmine directory
RUN mkdir /pocketmine-build
RUN cd /pocketmine-build && curl -sL http://get.pocketmine.net/ | bash -s - -r -v stable

# pocketmine's main UDP port
EXPOSE 19132

# script needed to work around docker/pocketmine limitations
COPY ./src/scripts/docker-start.sh /pocketmine-build/

RUN mkdir /pocketmine-build/plugins

WORKDIR /pocketmine-build
VOLUME /mnt/pocketmine
CMD [ "./docker-start.sh" ]