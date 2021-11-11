FROM phusion/baseimage:0.9.16
MAINTAINER hernando


# Set correct environment variables
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV TERM xterm

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Configure user nobody to match unRAID's settings
 RUN \
 usermod -u 99 nobody && \
 usermod -g 100 nobody && \
 usermod -d /home nobody && \
 chown -R nobody:users /home

# Disable SSH
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Installing Dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y software-properties-common python-software-properties 
RUN add-apt-repository -y ppa:webupd8team/java

RUN apt-get update
RUN apt-get install -y default-jre 
RUN apt-get install -y default-jdk 
	#RUN apt-get install -y oracle-java8-installer 
	#RUN apt-get install -y oracle-java8-set-default

RUN apt-get -y install screen python-cherrypy3 mc rdiff-backup git
RUN apt-get -y install openssh-server uuid pwgen

# Installing MineOS scripts
RUN mkdir -p /usr/games /var/games/minecraft
RUN  git clone git://github.com/hexparrot/mineos /usr/games/minecraft
WORKDIR /usr/games/minecraft
RUN chmod +x server.py mineos_console.py generate-sslcert.sh 
RUN ln -s /usr/games/minecraft/mineos_console.py /usr/local/bin/mineos

# Customize server settings
ADD mineos.conf /usr/games/minecraft/mineos.conf
ADD supervisor_conf.d/mineos.conf /etc/supervisor/conf.d/mineos.conf
ADD supervisor_conf.d/sshd.conf /etc/supervisor/conf.d/sshd.conf

RUN mkdir /var/games/minecraft/ssl_certs
RUN mkdir /var/games/minecraft/log
RUN mkdir /var/games/minecraft/run
RUN mkdir /var/run/sshd

# Add start script
ADD start.sh /usr/games/minecraft/start.sh
	#RUN chmod +x /usr/games/minecraft/start.sh

# Add minecraft user and change owner files.
RUN useradd -s /bin/bash -d /usr/games/minecraft -m minecraft
RUN usermod -G sudo minecraft
RUN sed -i 's/%sudo.*/%sudo   ALL=(ALL:ALL) NOPASSWD:ALL/' /etc/sudoers
RUN chown -R minecraft:minecraft /usr/games/minecraft /var/games/minecraft

# Cleaning
RUN apt-get clean

VOLUME /var/games/minecraft
WORKDIR /usr/games/minecraft
EXPOSE 22 8443 25565

ENTRYPOINT ["./start.sh"]
