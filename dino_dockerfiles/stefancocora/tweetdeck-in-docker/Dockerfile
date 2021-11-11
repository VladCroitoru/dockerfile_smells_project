FROM ubuntu:14.04

MAINTAINER Stefan Cocora <stefan.cocora@gmail.com>

ENV 	DEBIAN_FRONTEND noninteractive
ENV 	LANGUAGE en_US.UTF-8
ENV 	LANG en_US.UTF-8
ENV 	LC_ALL en_US.UTF-8

RUN apt-get update

RUN apt-get install -y openssh-server xubuntu-desktop

RUN add-apt-repository -y ppa:x2go/stable
RUN add-apt-repository -y ppa:ubuntu-wine/ppa

RUN sudo dpkg --add-architecture i386
RUN apt-get update

RUN apt-get install x2goserver x2goserver-xsession pwgen wine1.7 winetricks wine-gecko2.34 -y

RUN mkdir -p /var/run/sshd && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config
RUN sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config
RUN sed -i "s/#PasswordAuthentication/PasswordAuthentication/g" /etc/ssh/sshd_config

RUN mkdir -p /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix

# add user
RUN adduser --disabled-password --gecos "" tweetdeck && adduser tweetdeck sudo

# install lessmsi to extract the tweetdeck msi
RUN sudo -u tweetdeck sh -c "mkdir /tmp/lessmsi && \
                            wget https://github.com/activescott/lessmsi/releases/download/v1.2.0/lessmsi-v1.2.0.zip -O /tmp/lessmsi/lessmsi-v1.2.0.zip && \
                            cd /tmp/lessmsi && \
                            unzip lessmsi-v1.2.0.zip"

# install tweetdeck as tweetdeck user
# create wine prefix
USER tweetdeck
RUN WINEARCH=win32 WINEPREFIX=/home/tweetdeck/.winetweetdeck wine winecfg 2>&1
ADD install-tweetdeck.sh /var/tmp/install-tweetdeck.sh
RUN /var/tmp/install-tweetdeck.sh

USER root
ADD Tweetdeck-Logo.png /var/tmp/Tweetdeck-Logo.png
RUN chown -R tweetdeck:tweetdeck /var/tmp/Tweetdeck-Logo.png
ADD TweetDeck-xfce.desktop /home/tweetdeck/Desktop/TweetDeck.desktop
RUN chown -R tweetdeck:tweetdeck /home/tweetdeck/Desktop

ADD set_user_pw.sh /set_user_pw.sh
ADD run.sh /run.sh
RUN chmod +x /*.sh

EXPOSE 22
CMD ["/run.sh"]
