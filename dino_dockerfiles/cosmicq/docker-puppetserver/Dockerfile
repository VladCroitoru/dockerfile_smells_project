# Taken from puppetlabs/puppet-in-docker (puppetserver-standalone)
#
# This was converted from ubuntu to phusion/baseimage
#

FROM phusion/baseimage:0.9.22
MAINTAINER CosmicQ <cosmicq@cosmicegg.net>

ENV HOME /root
ENV LANG en_US.UTF-8

ENV PUPPETDB_TERMINUS_VERSION="5.1.3" PUPPET_SERVER_VERSION="5.1.3" DUMB_INIT_VERSION="1.2.0" UBUNTU_CODENAME="xenial" PUPPETSERVER_JAVA_ARGS="-Xms256m -Xmx256m" PATH=/opt/puppetlabs/server/bin:/opt/puppetlabs/puppet/bin:/opt/puppetlabs/bin:$PATH

LABEL org.label-schema.vendor="Puppet" \
      org.label-schema.url="https://github.com/puppetlabs/puppet-in-docker" \
      org.label-schema.name="Puppet Server" \
      org.label-schema.license="Apache-2.0" \
      org.label-schema.version=$PUPPET_SERVER_VERSION \
      org.label-schema.vcs-url="https://github.com/puppetlabs/puppet-in-docker" \
      org.label-schema.vcs-ref="897dbb17ad2194153ef09e5e9b684f17ceb019a2" \
      org.label-schema.build-date="2017-10-24T11:26:06Z" \
      org.label-schema.schema-version="1.0" \
      com.puppet.dockerfile="/Dockerfile"

RUN locale-gen en_US.UTF-8
RUN ln -s -f /bin/true /usr/bin/chfn

RUN apt-get update && apt-get -y upgrade &&\
    apt-get install -y wget=1.17.1-1ubuntu1 &&\
    wget https://apt.puppetlabs.com/puppet5-release-"$UBUNTU_CODENAME".deb &&\
    wget https://github.com/Yelp/dumb-init/releases/download/v"$DUMB_INIT_VERSION"/dumb-init_"$DUMB_INIT_VERSION"_amd64.deb &&\
    dpkg -i puppet5-release-"$UBUNTU_CODENAME".deb &&\
    dpkg -i dumb-init_"$DUMB_INIT_VERSION"_amd64.deb &&\
    rm puppet5-release-"$UBUNTU_CODENAME".deb dumb-init_"$DUMB_INIT_VERSION"_amd64.deb &&\
    apt-get update &&\
    apt-get install --no-install-recommends git -y puppetserver="$PUPPET_SERVER_VERSION"-1"$UBUNTU_CODENAME" &&\
    apt-get install --no-install-recommends -y puppetdb-termini="$PUPPETDB_TERMINUS_VERSION"-1"$UBUNTU_CODENAME" &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/* &&\
    gem install --no-rdoc --no-ri r10k

RUN puppet config set autosign true --section master

RUN rm -f /etc/service/sshd/down

COPY puppetserver /etc/default/puppetserver
COPY logback.xml /etc/puppetlabs/puppetserver/
COPY request-logging.xml /etc/puppetlabs/puppetserver/
COPY Dockerfile /

COPY start_puppetserver.sh /etc/service/puppetserver/run

EXPOSE 8140

VOLUME [ \
	"/etc/puppetlabs/code/", \
	"/etc/puppetlabs/puppet/", \
	"/opt/puppetlabs/server/data/puppetserver/" \
]

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
