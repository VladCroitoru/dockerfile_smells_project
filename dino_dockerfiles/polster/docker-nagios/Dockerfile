FROM centos:centos7

MAINTAINER Simon Dietschi

######################
# Build time arguments
######################

ARG NAGIOS_VERSION=${nagios_version:-4.2.4}
ARG NAGIOS_PLUGINS_VERSION=${nagios_version:-2.1.4}
ARG NAGIOS_NRPE_VERSION=${nagios_nrpe_version:-3.0.1}
ARG NAGIOS_ADMIN_USER=nagiosadmin
# Use the following command to generate the password: htpasswd -nb username password
# Default is nagiosadmin
ARG NAGIOS_ADMIN_PASSWORD=${nagios_admin_password:-'$apr1$MwEjgUy/$Y/USOaghUjLIxxg.Ww1C10'}

#######################
# Environment variables
#######################

ENV NAGIOS_HOME=/usr/local/nagios
ENV NAGIOS_USER=nagios
ENV NAGIOS_GROUP=nagios
ENV NAGIOS_CMDGROUP=nagcmd
ENV NAGIOSADMIN_USER=nagiosadmin

###############
# Prerequisites
###############

# Update
RUN yum -y update

# Install required packages
RUN yum -y install epel-release
# Permanent packages
RUN yum -y install wget httpd openssl php perl tar unzip sysstat supervisor
# Build/dev dependencies
RUN yum -y install gd gd-devel openssl-devel gcc glibc libmcrypt-devel make bc

# Create required users and groups
RUN groupadd $NAGIOS_GROUP && groupadd $NAGIOS_CMDGROUP
RUN useradd --system -d $NAGIOS_HOME -g $NAGIOS_GROUP $NAGIOS_USER
RUN usermod -a -G $NAGIOS_CMDGROUP $NAGIOS_USER
RUN usermod -a -G $NAGIOS_GROUP,$NAGIOS_CMDGROUP apache

#############
# Nagios Core
#############

# Download Nagios core
ADD https://assets.nagios.com/downloads/nagioscore/releases/nagios-$NAGIOS_VERSION.tar.gz /tmp

# Build and install Nagios
RUN cd /tmp/ && tar xf nagios-$NAGIOS_VERSION.tar.gz
RUN cd /tmp/nagios-$NAGIOS_VERSION && ./configure						\
  --prefix=${NAGIOS_HOME}					\
  --exec-prefix=${NAGIOS_HOME}				\
  --enable-event-broker					\
  --with-nagios-command-user=${NAGIOS_USER}		\
  --with-command-group=${NAGIOS_CMDGROUP}			\
  --with-nagios-user=${NAGIOS_USER}			\
  --with-nagios-group=${NAGIOS_GROUP}
RUN cd /tmp/nagios-$NAGIOS_VERSION && make all && make install && make install-init
RUN cd /tmp/nagios-$NAGIOS_VERSION && make install-config && make install-commandmode && make install-webconf

RUN cd /tmp/nagios-$NAGIOS_VERSION && cp -R contrib/eventhandlers/ ${NAGIOS_HOME}/libexec/
RUN chown -R ${NAGIOS_USER}:${NAGIOS_GROUP} ${NAGIOS_HOME}/libexec/eventhandlers

################
# Nagios Plugins
################

# Download Nagios plugins
ADD https://nagios-plugins.org/download/nagios-plugins-$NAGIOS_PLUGINS_VERSION.tar.gz /tmp

# Build and install Nagios plugins
RUN cd /tmp && tar xf nagios-plugins-$NAGIOS_PLUGINS_VERSION.tar.gz
RUN cd /tmp/nagios-plugins-$NAGIOS_PLUGINS_VERSION && ./configure \
  --prefix=${NAGIOS_HOME} \
  --with-nagios-user=${NAGIOS_USER}			\
  --with-nagios-group=${NAGIOS_GROUP}
RUN cd /tmp/nagios-plugins-$NAGIOS_PLUGINS_VERSION && make && make install

###########
# Additions
###########

# Download additions
ADD https://github.com/NagiosEnterprises/nrpe/releases/download/$NAGIOS_NRPE_VERSION/nrpe-$NAGIOS_NRPE_VERSION.tar.gz /tmp

# Build and install NRPE (check_nrpe)
RUN cd /tmp/ && tar xf nrpe-$NAGIOS_NRPE_VERSION.tar.gz
RUN cd /tmp/nrpe-$NAGIOS_NRPE_VERSION && ./configure \
  --enable-command-args \
  --libexecdir=${NAGIOS_HOME}/libexec/ \
  --with-nagios-user=${NAGIOS_USER} \
  --with-nagios-group=${NAGIOS_GROUP}
RUN cd /tmp/nrpe-$NAGIOS_NRPE_VERSION && make check_nrpe && make install-plugin

###############
# Nagios Config
###############

# Create initial Nagios config
RUN ${NAGIOS_HOME}/bin/nagios -v ${NAGIOS_HOME}/etc/nagios.cfg

# Configure the Nagios default admin user
RUN echo "$NAGIOS_ADMIN_USER:$NAGIOS_ADMIN_PASSWORD" > ${NAGIOS_HOME}/etc/htpasswd.users
RUN chown ${NAGIOS_USER}:${NAGIOS_GROUP} ${NAGIOS_HOME}/etc/htpasswd.users

#########
# Cleanup
#########

# Remove no longer needed support packages
RUN yum -y remove gcc

##################
# Container Config
##################

# Expose required ports
# web
EXPOSE 80
# mail
EXPOSE 25
# nrpe
EXPOSE 5666

# Add the supervisor config
COPY supervisord.conf /etc/supervisord.conf

# start up
CMD ["/usr/bin/supervisord"]
