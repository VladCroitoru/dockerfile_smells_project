# Docker base-image for providing Glassfish 3.1.2.2 server running on 1.7 JDK.
#
#     https://github.com/reap/docker-glassfish3
#
FROM phusion/baseimage:0.9.11
MAINTAINER Ilari Liukko "ilari.liukko@iki.fi"

# Set correct environment variables.
ENV HOME /root

# install necessary applications
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y unzip
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y expect

# Install OpenJDK 1.7 version 51
# newest version has bug in corba-implementation which affects Glassfish.
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends openjdk-7-jre-headless=7u51-2.4.6-1ubuntu4
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends openjdk-7-jre=7u51-2.4.6-1ubuntu4
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends openjdk-7-jdk=7u51-2.4.6-1ubuntu4

ADD glassfish-3.1.2.2-silent-installation-answers /glassfish-3.1.2.2-silent-installation-answers

# Load and install Glassfish
RUN wget --no-cookies --no-check-certificate "http://download.java.net/glassfish/3.1.2.2/release/glassfish-3.1.2.2-unix.sh" -O /tmp/glassfish-3.1.2.2-unix.sh
RUN sh /tmp/glassfish-3.1.2.2-unix.sh -s -a /glassfish-3.1.2.2-silent-installation-answers

RUN echo /opt/glassfish3 > /etc/container_environment/GLASSFISH_HOME
ENV GLASSFISH_HOME /opt/glassfish3

RUN wget -q --no-cookies --no-check-certificate "http://jdbc.postgresql.org/download/postgresql-9.3-1102.jdbc4.jar" -O /opt/glassfish3/glassfish/lib/postgresql-9.1-903.jdbc4.jar

ADD create_domain.sh /create_domain.sh
ADD glassfish.passwords /glassfish.passwords

RUN chmod +x /*.sh

# expose http-port and admin console port of default domain (domain1)
EXPOSE 4848 8080

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
