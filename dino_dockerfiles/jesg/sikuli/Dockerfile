
FROM debian:wheezy

MAINTAINER Jason Gowan <gowanjason@gmail.com>

RUN groupadd sikuli && useradd -m -g sikuli -s /bin/bash sikuli --create-home

RUN apt-get -y update

RUN apt-get -y install x11vnc libsikuli-script-java tightvncserver

RUN mkdir /home/sikuli/.vnc
ADD ./xstartup /home/sikuli/.vnc/xstartup
RUN chmod -v +x /home/sikuli/.vnc/xstartup
RUN x11vnc -storepasswd secret /home/sikuli/.vnc/passwd
RUN chown -R sikuli:sikuli /home/sikuli/.vnc

