#
# doomkin/docker-oracle-xe-11g Dockerfile
#
# https://github.com/doomkin/docker-oracle-xe-11g
#
# Based on:
# https://github.com/doomkin/ubuntu-ssh
# https://github.com/wnameless/docker-oracle-xe-11g
#

# Pull base image
FROM doomkin/ubuntu-ssh
MAINTAINER Pavel Doomkin

# Set the noninteractive frontend
ENV DEBIAN_FRONTEND noninteractive

# Update packages
RUN apt-get update && apt-get upgrade -y

# Copy external files
ADD chkconfig /sbin/chkconfig
ADD init.ora /
ADD initXETemp.ora /
ADD oracle-xe_11.2.0-1.0_amd64.debaa /
ADD oracle-xe_11.2.0-1.0_amd64.debab /
ADD oracle-xe_11.2.0-1.0_amd64.debac /
# ADD oracle-xe_11.2.0-1.0_amd64.deb /
RUN cat /oracle-xe_11.2.0-1.0_amd64.deba* > /oracle-xe_11.2.0-1.0_amd64.deb

# Prepare to install Oracle
RUN apt-get install -y libaio1 net-tools bc && \
    ln -s /usr/bin/awk /bin/awk && \
    mkdir /var/lock/subsys && \
    chmod 755 /sbin/chkconfig

# Install Oracle
RUN dpkg --install /oracle-xe_11.2.0-1.0_amd64.deb

RUN mv /init.ora /u01/app/oracle/product/11.2.0/xe/config/scripts
RUN mv /initXETemp.ora /u01/app/oracle/product/11.2.0/xe/config/scripts

RUN printf 8080\\n1521\\noracle\\noracle\\ny\\n | /etc/init.d/oracle-xe configure

RUN echo 'export ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe' >> /etc/bash.bashrc
RUN echo 'export PATH=$ORACLE_HOME/bin:$PATH' >> /etc/bash.bashrc
RUN echo 'export ORACLE_SID=XE' >> /etc/bash.bashrc

# Cleanup
RUN rm /oracle-xe_11.2.0-1.0_amd64.deb* && \
    rm -rf /var/lib/apt/lists/*

# Expose ports
EXPOSE 1521 8080

# Startup
CMD sed -i -E "s/HOST = [^)]+/HOST = $HOSTNAME/g" /u01/app/oracle/product/11.2.0/xe/network/admin/listener.ora; \
    service oracle-xe start; \
    /usr/sbin/sshd -D
