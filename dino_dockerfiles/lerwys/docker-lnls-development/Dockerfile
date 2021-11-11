FROM jboss/base-jdk:8

MAINTAINER Lucas Russo

# User root user to install software
USER root

# Create default admin user
RUN echo nameserver 10.0.0.71 >> /etc/resolv.conf && \
    yum -y install git maven vim && yum clean all

RUN mkdir -p /opt/lnls
RUN mkdir -p /opt/lnls/deploy

WORKDIR /opt/lnls/

# Switch back to jboss user
USER jboss

