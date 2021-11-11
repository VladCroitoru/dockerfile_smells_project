FROM dorowu/ubuntu-desktop-lxde-vnc
MAINTAINER Mark Fernandes <mark.fernandes@ifr.ac.uk>
# Environment to deliver Harvest utils tutorial (Parsnp, Gingr) using  LXDE and VNC server under Docker
# See http://harvest.readthedocs.io/en/latest/index.html#
RUN REL="$(lsb_release -c -s)"
# Add the appropriate repositories including CRAN
RUN \
	  apt-get update && \
	  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \
	   apt-get install -y  software-properties-common && \
	add-apt-repository  "deb http://archive.ubuntu.com/ubuntu trusty universe" && \
	add-apt-repository  "deb http://archive.ubuntu.com/ubuntu trusty main restricted universe multiverse" && \
	add-apt-repository  "deb http://archive.ubuntu.com/ubuntu trusty-updates main restricted universe multiverse" && \
	add-apt-repository  "deb http://archive.ubuntu.com/ubuntu trusty-backports main restricted universe multiverse" && \
	add-apt-repository  "deb http://cran.ma.imperial.ac.uk/bin/linux/ubuntu trusty/"

 RUN apt-get update && apt-get install -y wget git unzip gzip tar xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic && \
        rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 
# We need xfonts installing otherwise gingr menus become squares :-(
RUN mkdir /harvest && cd /harvest && wget https://github.com/marbl/harvest/releases/download/v1.1.2/Harvest-Linux64-v1.1.2.tar.gz
RUN tar -xvf /harvest/*.tar.gz
# create Soft link to utilities
RUN ln -s /root/Harvest-Linux64-v1.1.2/* /usr/local/bin/
RUN mkdir /scripts && mkdir /home/ubuntu /home/ubuntu/.config /home/ubuntu/.config/autostart
# can add scripts and a startup web-page from here
# ADD /scripts/* /scripts/
# ADD /autostarts/.desktop /home/ubuntu/.config/autostart/.desktop
# RUN chmod +x /scripts/* && ln -s /scripts/* /usr/local/bin/

# Local writable volume as a work directory
VOLUME /Coursedata
