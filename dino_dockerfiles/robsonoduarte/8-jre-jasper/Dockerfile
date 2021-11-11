FROM openjdk:8-jre
MAINTAINER robsonoduarte

RUN  apt-get update

# add time zone of america/zone
RUN echo "America/Sao_Paulo" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

# add locale pt-br
RUN apt-get update \
	&& apt-get install -y locales \
        && localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8
ENV LANG pt_BR.UTF8
ENV LANGUAGE pt_BR:pt  
ENV LC_ALL pt_BR.UTF-8 


# add ms core fonts
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe multiverse" > /etc/apt/sources.list
RUN apt-get update
RUN yes | apt-get install -y --force-yes ttf-mscorefonts-installer


# clean .deb files and apt lists
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
