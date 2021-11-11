################################################################################
# mesos-slave:1.2.0
# Date: 1/21/2016
# Docker Version: 1.9.1~trusty
# Mesos Version: 0.26.0-0.2.145.ubuntu1404
#
# Description:
# Mesos slave container with docker-engine installed. With Docker moving away
# from a monolithic binary, docker-engine must now be installed within the
# container itself. 
################################################################################

FROM mrbobbytables/mesos-base:1.2.0

MAINTAINER Bob Killen / killen.bob@gmail.com / @mrbobbytables


ENV VERSION_DOCKER=1.9.1-0~trusty

RUN apt-get update                           \
 && apt-get -y install apt-transport-https   \
 && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 2C52609D  \
 && echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" >> /etc/apt/sources.list.d/docker.list \
 && apt-get update                 \
 && apt-get -y install             \
    docker-engine=$VERSION_DOCKER  \
 && apt-get -y autoremove          \
 && apt-get -y autoclean           \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

COPY ./skel /

RUN chmod +x ./init.sh  \
 && chown -R logstash-forwarder:logstash-forwarder /opt/logstash-forwarder

EXPOSE 5051

 CMD ["./init.sh"]
