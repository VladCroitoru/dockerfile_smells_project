FROM phusion/baseimage:0.9.22
MAINTAINER CosmicQ <cosmicq@cosmicegg.net>

ENV HOME /root
ENV LANG en_US.UTF-8

ENV PUPPETDB_VERSION="5.1.1" PUPPET_AGENT_VERSION="5.3.2" DUMB_INIT_VERSION="1.2.0" UBUNTU_CODENAME="xenial" PUPPETDB_DATABASE_CONNECTION="//postgres:5432/puppetdb" PUPPETDB_USER=puppetdb PUPPETDB_PASSWORD=puppetdb PUPPETDB_JAVA_ARGS="-Djava.net.preferIPv4Stack=true -Xms256m -Xmx256m" PATH=/opt/puppetlabs/server/bin:/opt/puppetlabs/puppet/bin:/opt/puppetlabs/bin:$PATH

LABEL org.label-schema.vendor="Puppet" \
      org.label-schema.url="https://github.com/puppetlabs/puppet-in-docker" \
      org.label-schema.name="PuppetDB" \
      org.label-schema.license="Apache-2.0" \
      org.label-schema.version=$PUPPETDB_VERSION \
      org.label-schema.vcs-url="https://github.com/puppetlabs/puppet-in-docker" \
      org.label-schema.vcs-ref="897dbb17ad2194153ef09e5e9b684f17ceb019a2" \
      org.label-schema.build-date="2017-10-24T11:26:06Z" \
      org.label-schema.schema-version="1.0" \
      com.puppet.dockerfile="/Dockerfile"

RUN locale-gen en_US.UTF-8
RUN ln -s -f /bin/true /usr/bin/chfn

RUN apt-get update && \
    apt-get install -y wget netcat lsb-release && \
    wget https://apt.puppetlabs.com/puppet5-release-"$UBUNTU_CODENAME".deb && \
    wget https://github.com/Yelp/dumb-init/releases/download/v"$DUMB_INIT_VERSION"/dumb-init_"$DUMB_INIT_VERSION"_amd64.deb && \
    dpkg -i puppet5-release-"$UBUNTU_CODENAME".deb && \
    dpkg -i dumb-init_"$DUMB_INIT_VERSION"_amd64.deb && \
    rm puppet5-release-"$UBUNTU_CODENAME".deb dumb-init_"$DUMB_INIT_VERSION"_amd64.deb && \
    apt-get update && \
    apt-get install --no-install-recommends -y puppet-agent="$PUPPET_AGENT_VERSION"-1"$UBUNTU_CODENAME" puppetdb="$PUPPETDB_VERSION"-1puppetlabs1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY puppetdb /etc/default/
COPY logging /etc/puppetlabs/puppetdb/logging

RUN rm -fr /etc/puppetlabs/puppetdb/conf.d
COPY conf.d /etc/puppetlabs/defaults/conf.d

# Persist the agent SSL certificate.
VOLUME /etc/puppetlabs/puppet/ssl/
# /etc/puppetlabs/puppetdb/ssl is automatically populated from here and
# doesn't need a separate volume.
VOLUME /etc/puppetlabs/puppetdb/conf.d

COPY start_puppetdb.sh /etc/service/puppetdb/run

EXPOSE 8080 8081

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
