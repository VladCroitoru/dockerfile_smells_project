FROM debian:jessie
MAINTAINER xxaxxelxx <x@axxel.net>

#RUN sed -e 's/$/ contrib non-free/' -i /etc/apt/sources.list 

RUN apt-get -qq -y update
RUN apt-get -qq -y dist-upgrade

ENV TERM=xterm
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -qq -y install ssh
RUN apt-get -qq -y install sudo
RUN apt-get -qq -y install rsync
RUN apt-get -qq -y install mc

# clean up
RUN apt-get clean

RUN mkdir /var/run/sshd

RUN useradd -m -g nogroup depot
RUN sudo -u depot mkdir /home/depot/.ssh
COPY authorized_keys2 /home/depot/.ssh/
RUN chown -R depot:nogroup /home/depot/.ssh
RUN sudo -u depot chmod -R 700 /home/depot/.ssh

#RUN mkdir -p /depot
#RUN chown depot /depot
#RUN chmod 700 /depot

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
#CMD [ "bash" ]
