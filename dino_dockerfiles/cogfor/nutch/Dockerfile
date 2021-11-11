# Apache Nutch
#
# VERSION 20160613_1

FROM cogfor/hbase:0.98-hadoop2

MAINTAINER Rene Nederhand <rene@cogfor.com>

# Set correct environment variables.
ENV HOME /root
WORKDIR /

# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Install various dependencies
RUN apt-get update && apt-get install -y ant git curl build-essential vim 

# Set up JAVA_HOME
#RUN echo 'export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")' >> $HOME/.bashrc

# Checkout Release
RUN git clone -b release-2.3.1 https://github.com/apache/nutch.git nutch_source && cd nutch_source

WORKDIR /nutch_source

# Apply configuration
## Set storage backend: HBase
ADD conf/hbase-site.xml /nutch_source/conf
## Configure HBase adapter
ADD conf/gora.properties /nutch_source/conf
## Set spider and configure storage
ADD conf/nutch-site.xml /nutch_source/conf
## Build gora-hbase dependency
RUN vim -c 'g/name="gora-hbase"/+1d' -c 'x' ivy/ivy.xml
RUN vim -c 'g/name="gora-hbase"/-1d' -c 'x' ivy/ivy.xml

# Build Nutch
RUN ant

# Create data folder for HBase
RUN mkdir /data

# Convenience symlink to Nutch runtime local
RUN ln -s nutch_source/runtime/local /$HOME/nutch

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
