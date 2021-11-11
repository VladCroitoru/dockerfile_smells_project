FROM ubuntu:18.04

MAINTAINER binerf <seedbox@mygaia.org>

# Base settings
ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root

# Install base packages
RUN apt-get update -y
RUN apt-get install software-properties-common \
	sudo \
	-y

# Add PPA Repository
#RUN echo "deb http://ppa.launchpad.net/transmissionbt/ppa/ubuntu bionic main" > /etc/apt/sources.list.d/transmissionbt-ppa-bionic.list
RUN add-apt-repository ppa:transmissionbt/ppa -y

# Update package lists
RUN apt-get update -y
RUN apt-get -y dist-upgrade

# Install transmission
RUN apt-get install transmission-cli \
	transmission-common \
	transmission-daemon \
	-y

VOLUME /var/lib/transmission-daemon
RUN chown -R debian-transmission:debian-transmission /var/lib/transmission-daemon

ADD run.sh /run.sh
RUN chmod 0755 /run.sh

#Slimming down Docker containers
RUN apt-get purge \
	cpp \
	build-essential \
	eject \
	g++-4.8 \
	libstdc++-4.8-dev \
	make \
	manpages \
	manpages-dev \
	vim-common \
	vim-tiny \
	-y

RUN apt-get autoremove -y
RUN apt-get clean -y
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#Set upstart command
CMD ["/run.sh"]

#Expose ports
EXPOSE 9091
EXPOSE 51413
