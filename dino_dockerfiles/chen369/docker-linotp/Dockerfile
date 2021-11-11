FROM debian:latest
MAINTAINER Chen Chiu <docker-maintainer@blitzcorp.org>
ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

RUN     apt-get update 
RUN	apt-get -y install gnupg
RUN	echo 'deb http://www.linotp.org/apt/debian jessie linotp' >> /etc/apt/sources.list
RUN     gpg --keyserver keys.gnupg.net --recv-keys 913DFF12F86258E5
RUN     gpg --export 913DFF12F86258E5 | apt-key add - 
RUN	apt-get update
RUN	apt-get -y install linotp linotp-useridresolver wget python-ldap 
RUN     apt-get -y install linotp-smsprovider linotp-adminclient-cli linotp-adminclient-gui libpam-linotp
	

EXPOSE 80 443 5347
