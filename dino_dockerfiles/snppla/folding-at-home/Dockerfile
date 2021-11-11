# Folding@home
#
# VERSION               0.1
# Run with: docker run -d -t -i jordan0day/folding-at-home
# Inspired by magglass1/docker-folding-at-home

# Set environment variables USERNAME, TEAM, and POWER to customize your Folding client.

FROM centos:7

# If you set USERNAME to Anonymous, the folding@home client pauses for 5 minutes, but will then begin processing data.
ENV USERNAME Anonymous
ENV TEAM 0
ENV POWER medium
ENV PASSKEY=

# Install updates
RUN yum update -y

# Install Folding@home
RUN rpm -i https://download.foldingathome.org/releases/public/release/fahclient/centos-6.7-64bit/v7.5/fahclient-7.5.1-1.x86_64.rpm
ADD config.xml /etc/fahclient/
ADD run.sh /run.sh
RUN chown fahclient:root /etc/fahclient/config.xml

CMD /run.sh

