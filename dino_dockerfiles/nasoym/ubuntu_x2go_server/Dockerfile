FROM nasoym/docker_ubuntu_sshd:latest
MAINTAINER Sinan Goo

RUN echo "deb http://ppa.launchpad.net/x2go/stable/ubuntu xenial main" >> /etc/apt/sources.list 
RUN echo "deb-src http://ppa.launchpad.net/x2go/stable/ubuntu xenial main" >> /etc/apt/sources.list
RUN apt-get install -y software-properties-common && add-apt-repository -y ppa:x2go/stable && apt-get update && apt-get purge -y software-properties-common && apt-get autoremove -y
RUN echo "XKBMODEL='pc105'" >> /etc/default/keyboard
RUN echo "XKBLAYOUT='us'" >> /etc/default/keyboard
RUN echo "XKBVARIANT=''" >> /etc/default/keyboard
RUN echo "XKBOPTIONS=''" >> /etc/default/keyboard
RUN echo "BACKSPACE='guess'" >> /etc/default/keyboard

RUN apt-get install -y x2goserver x2goserver-xsession

CMD service x2goserver start && /usr/sbin/sshd -D

