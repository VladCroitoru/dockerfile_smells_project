FROM ubuntu:14.04
MAINTAINER Javier Cabezas <jcabezasgivica@gmail.com> y Eugenio F. González <eugeniofidel@gmail.com>

ENV VERSION 2.2.0
ENV USERNAME admin
ENV PASSWORD admin

# Java,curl and wget installations 
# Archiva file download, decompression and copy of all the files to folder /opt


RUN sudo apt-get update \
        && sudo apt-get -y install openjdk-7-jre-headless \
        && sudo apt-get -y install curl \
        && sudo apt-get -y install wget \
        && wget -c http://ftp.cixug.es/apache/archiva/$VERSION/binaries/apache-archiva-$VERSION-bin.tar.gz \
        && tar xfv apache-archiva-$VERSION-bin.tar.gz \
        && sudo mv apache-archiva-$VERSION /opt/

#
# Set up of the working directory in which Archiva security configuration file is found
#

 WORKDIR /opt/apache-archiva-$VERSION/conf/

#
# Copy of the script into the working folder
#

COPY entrypoint.sh /opt/apache-archiva-$VERSION/conf/
 
#
# Set up of required permissions on script file 
#

RUN chmod 777 entrypoint.sh


ENTRYPOINT bash -C './entrypoint.sh';'bash'

