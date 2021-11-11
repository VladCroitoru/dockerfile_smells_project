FROM centos:latest
MAINTAINER Pika Do <pokido99@gmail.com>

# Proxy settings if necessary
# ENV http_proxy=http://proxy:8080
# ENV https_proxy=http://proxy:8080
# ENV no_proxy="127.0.0.1,localhost,.mydomain.com"

# Update system
RUN yum -y update

# Install Couchbase
ENV CB_VERSION 2.2.0
ENV CB_USER couchbase
RUN yum -y install http://packages.couchbase.com/releases/${CB_VERSION}/couchbase-server-community_${CB_VERSION}_x86_64.rpm
USER $CB_USER
COPY run.sh /

# Set default command
CMD /run.sh
EXPOSE 8091 8092 11209 11210 11211
