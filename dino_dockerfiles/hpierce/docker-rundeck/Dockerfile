#
# Dockerfile
#
#
FROM hpierce/docker-ubuntu-16.04-base-java7

# Environment
ENV DEBIAN_FRONTEND noninteractive
ENV RUNDECK_VERSION 2.6.9-1

# rundeck install
ADD http://dl.bintray.com/rundeck/rundeck-deb/rundeck-${RUNDECK_VERSION}-GA.deb /tmp/rundeck.deb
RUN dpkg -i /tmp/rundeck.deb && rm /tmp/rundeck.deb

# Add keys
ADD .ssh /var/lib/rundeck/.ssh 
RUN chown -R rundeck:rundeck /var/lib/rundeck

# Scripts for RunDeck
COPY change_admin_pass.sh /root
COPY change_localhost.sh /root

# ports
EXPOSE 4440 4443

ENTRYPOINT /etc/init.d/rundeckd start && /bin/bash

