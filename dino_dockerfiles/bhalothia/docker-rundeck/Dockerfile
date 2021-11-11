
# Dockerfile for docker image of RunDeck
# https://github.com/bhalothia/docker-rundeck
# RunDeck plugins from https://github.com/rundeck-plugins

FROM debian:wheezy
MAINTAINER Virendra Singh Bhalothia <bhalothia@theremotelab.com>

#ENV DEBIAN_FRONTEND noninteractive
ENV SERVER_URL http://localhost:4440
ENV RDECK_BASE /var/lib/rundeck

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update && apt-get -qqy upgrade && apt-get -qqy install --no-install-recommends bash supervisor procps sudo ca-certificates openjdk-7-jre-headless openssh-client mysql-server mysql-client pwgen curl git && apt-get clean

ADD http://dl.bintray.com/rundeck/rundeck-deb/rundeck-2.5.3-1-GA.deb /tmp/rundeck.deb

ADD prerequisites/ /

RUN dpkg -i /tmp/rundeck.deb && rm /tmp/rundeck.deb
RUN chown rundeck:rundeck /tmp/rundeck
RUN chmod u+x /opt/run
RUN mkdir -p $RDECK_BASE/.ssh
RUN chown rundeck:rundeck $RDECK_BASE/.ssh

# Supervisor Settings
RUN mkdir -p /var/log/supervisor && mkdir -p /opt/supervisor
RUN chmod u+x /opt/supervisor/rundeck && chmod u+x /opt/supervisor/mysql_supervisor

EXPOSE 4440 4443

VOLUME  ["/etc/rundeck", "/var/rundeck", "/var/lib/rundeck", "/var/lib/mysql", "/var/log/rundeck"]

# Start Supervisor
ENTRYPOINT ["/opt/run"]
