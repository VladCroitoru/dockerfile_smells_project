FROM ubuntu

MAINTAINER togashik

# ENTRYPOINT
ADD entrypoint.sh /entrypoint.sh

# Use jaist.ac.jp repo
RUN sed -i 's|http://archive.ubuntu.com/ubuntu|http://ftp.jaist.ac.jp/pub/Linux/ubuntu|g' /etc/apt/sources.list

# Japanese langage settings
ENV DEBCONF_NONINTERACTIVE_SEEN true 
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get -y install build-essential
RUN apt-get -y install git wget curl vim locate
RUN apt-get -y install python
RUN apt-get -y install language-pack-ja-base language-pack-ja ibus-mozc
RUN apt-get -y install man
RUN apt-get -y install manpages-ja
RUN update-locale LANG=ja_JP.UTF-8 LANGUAGE=ja_JP:ja
ENV LANG ja_JP.UTF-8
ENV LC_ALL ja_JP.UTF-8
ENV LC_CTYPE ja_JP.UTF-8

# Java
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -y oracle-java8-installer

# Selenium
RUN adduser selenium
WORKDIR /home/selenium
RUN wget -O selenium-standalone.jar http://goo.gl/IHP6Qw

# Ubuntu DeskTop
RUN apt-get install -y xfce4 tightvncserver language-pack-ja fonts-vlgothic firefox

# Firefox Profile
ADD .mozilla /root/.mozilla

# VNC Password
RUN mkdir /root/.vnc
ADD .vnc/passwd /root/.vnc/passwd
RUN chmod 600 /root/.vnc/passwd

ENTRYPOINT ["sh", "/entrypoint.sh"]
