FROM 1and1internet/ubuntu-16-apache:latest
MAINTAINER christopher.james@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive
RUN \
  apt-get -qq -y clean && \
  apt-get -qq update && \
  apt-get -qq install -y libapache2-mod-perl2 libcgi-pm-perl liblocal-lib-perl cpanminus make gcc libexpat1-dev rsync libapache2-mod-perl2-dev && \
  /usr/sbin/a2enmod cgid && \
  rm -rf /var/lib/apt/lists/*
COPY files /
EXPOSE 8080
#USER 27
