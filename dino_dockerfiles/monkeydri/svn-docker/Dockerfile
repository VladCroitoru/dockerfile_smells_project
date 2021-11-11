FROM phusion/baseimage:0.9.18
MAINTAINER monkeydri <monkeydri@users.noreply.github.com>

ENV HOME /root

# Disable SSH
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Configure apt
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu/ precise universe' >> /etc/apt/sources.list
RUN apt-get -y update

# Install subversion and git including git-svn (to mirror svn repos onto a git remote) and expect to input ssh key passphrase in script
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y subversion git git-svn expect

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Default configuration: can be overridden at the docker command line
ENV SVN_REPONAME repos

EXPOSE 3690

RUN mkdir /etc/service/svn
ADD svn.sh /etc/service/svn/run
RUN chmod u+x /etc/service/svn/run

RUN mkdir -p /var/svn
RUN svnadmin create /var/svn/$SVN_REPONAME
ADD svnserve.conf /var/svn/$SVN_REPONAME/conf/svnserve.conf

# To store the data outside the container, mount /svn as a data volume
VOLUME /var/svn
