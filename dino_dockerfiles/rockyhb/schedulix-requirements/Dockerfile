FROM centos:7
MAINTAINER Claas Rockmann-Buchterkirche <claas@rockbu.de>
RUN rpm -Uvh "https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm"
RUN yum clean all
RUN yum -y update
RUN yum -y install java-1.7.0-openjdk-devel gcc gcc-c++ make jna wget git unzip
RUN rpm -Uvh "http://sourceforge.net/projects/jflex/files/jflex/1.4.1/jflex-1.4.1-0.rpm/download"
WORKDIR /tmp
RUN wget "http://eclipse.mirror.triple-it.nl/eclipse/downloads/drops4/R-4.5-201506032000/swt-4.5-gtk-linux-x86_64.zip"
RUN unzip swt-4.5-gtk-linux-x86_64.zip swt.jar
# COPY swt.jar /usr/share/java/
# RUN useradd schedulix
# RUN echo Done.
CMD /bin/bash
