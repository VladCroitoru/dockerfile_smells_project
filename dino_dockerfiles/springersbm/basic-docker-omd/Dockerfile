# Basic OMD installation for testing
# ==================================
#
#  * Based on Ubuntu 13.10 (backport of phusion/baseimage-docker)
#  * Installs OMD from http://labs.consol.de/repo/stable (only has omd for ubuntu 13.10)
#  * Installs check_mk_agent in docker itself
#  * Creates a initial master site in OMD
#
FROM      springersbm/phusion-baseimage-ubuntu-13.10:latest
MAINTAINER Springer Platform Engineering Team <platform-engineering@springer.com>
MAINTAINER Hector Rivas <hector.rivas@springer.com>

# This image is for testing OMD, so it is nice to have a shell
ENTRYPOINT /sbin/my_init -- bash -l

EXPOSE 22 80 6556

#####################################################################################
# Install OMD from the repository http://labs.consol.de/repo/stable
# 

# First register the new repo
RUN gpg --keyserver keys.gnupg.net --recv-keys F8C1CA08A57B9ED7
RUN gpg --armor --export F8C1CA08A57B9ED7 | apt-key add -
RUN echo 'deb http://labs.consol.de/repo/stable/ubuntu saucy main' >> /etc/apt/sources.list

# Install OMD
RUN apt-get update
RUN apt-get -y install omd

# Install some tooling
RUN apt-get -y install net-tools netcat xinetd wget 

# Install the agent to monitor localhost
RUN wget http://mathias-kettner.de/download/check-mk-agent_1.2.4p5-2_all.deb -P /tmp/
RUN dpkg -i /tmp/check-mk-agent_1.2.4p5-2_all.deb

# Fix some stuff in apache: no change ulimit and give the server a name
RUN echo "APACHE_ULIMIT_MAX_FILES=true" >> /etc/apache2/envvars
RUN echo ServerName basic-docker-omd > /etc/apache2/conf-available/docker-servername.conf
RUN a2enconf docker-servername

# Fix warning in syslog-ng in ubuntu 13.10: https://bugs.launchpad.net/ubuntu/+source/syslog-ng/+bug/1009920
RUN sed -i 's/^SYSLOGNG_OPTS.*/SYSLOGNG_OPTS="--no-caps --default-modules=affile,afprog,afsocket,afuser,basicfuncs,csvparser,dbparser,syslogformat"/' /etc/default/syslog-ng

#####################################################################################
# Setup the initial OMD site 'master'
#
# This method is a little bit hacky, and I had to do some workarounds:
#  1. tmpfs is not supported by standard docker (can be recompiled). 
#    In OMD can be disabled, but I don't know how to do it before initilize the site. 
#
#    Solution: try to create the site and change the config after.
# 
#  2. Second issue: the new user created by OMD needs to be in the group crontab 
#     to be able to change the cronjobs. But you need first to get the user to change it!
#    
# Any about this feedback is appreciated.
#

# Create master site.  Will fail, as commented
RUN omd create master || true

# Disable the TMPFS in the new generated site conf... hacky, hacky :)
RUN sed "s/CONFIG_TMPFS='on'/CONFIG_TMPFS='off'/" -i /omd/sites/master/etc/omd/site.conf 

# Add the new user to crontab, to avoid error merging crontabs
RUN adduser master crontab 

# OK, now the site starts :)
RUN omd start master

#####################################################################################
# Initial configuration of the site and image

# Add localhost as node monitored
ADD hosts.mk /omd/sites/master/etc/check_mk/conf.d/wato/hosts.mk

# First OMD service discovery and compile
RUN /etc/init.d/xinetd start && su - master -c "cmk -II"
RUN su - master -c "cmk -R"

# Fix some permission issues (not sure why it happens)
RUN chown -R master.master /omd/sites/master

#####################################################################################
# Other stuff
# Generate the SSH keys of the server
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Copy ssh key for root and master
RUN mkdir -p /omd/sites/master/.ssh /root/.ssh
ADD ssh/id_rsa /root/.ssh/id_rsa
ADD ssh/id_rsa.pub /root/.ssh/id_rsa.pub
ADD ssh/id_rsa.pub /root/.ssh/authorized_keys
ADD ssh/id_rsa /omd/sites/master/.ssh/id_rsa
ADD ssh/id_rsa.pub /omd/sites/master/.ssh/id_rsa.pub
ADD ssh/id_rsa.pub /omd/sites/master/.ssh/authorized_keys
RUN chmod 400 /root/.ssh/id_rsa /omd/sites/master/.ssh/id_rsa 

# Utility script to print the ssh key
# The user can use: docker run --entrypoint="/usr/bin/print_ssh_private_key" <image>
ADD print_ssh_private_key /usr/bin/print_ssh_private_key

# Unlock the user master to allow SSH access
RUN usermod -p master1 master
RUN passwd -u master

# Add scripts to start services in baseimage my_init:
ADD 10_startup_base_services /etc/my_init.d/10_startup_base_services
ADD 20_startup_omd_master /etc/my_init.d/20_startup_omd_master
