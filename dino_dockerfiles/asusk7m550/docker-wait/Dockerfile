FROM       centos:latest
MAINTAINER Jasper Aikema <jaikema@it-ernity.nl>

# Update base image
RUN yum -y update && yum clean all

# Install software
RUN yum -y install bind-utils iproute

# Add start.sh
COPY start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

# Sleep for 60m then exit
CMD ["/usr/local/bin/start.sh"]
