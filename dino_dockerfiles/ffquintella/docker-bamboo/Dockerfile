FROM ffquintella/docker-puppet:1.4.1

MAINTAINER Felipe Quintella <docker-bamboo@felipe.quintella.email>

LABEL version="6.7.1.1"
LABEL description="This image contais the bamboo application to be used \
as a server."


ENV LANG=C
ENV LANGUAGE=C
ENV LC_ALL=C

ENV JAVA_HOME "/opt/java_home/current"

ENV FACTER_JAVA_HOME "/opt/java_home"
ENV FACTER_JAVA_VERSION "8"
ENV FACTER_JAVA_VERSION_UPDATE "192"
ENV FACTER_JAVA_VERSION_BUILD "12"
ENV FACTER_JAVA_VERSION_HASH "750e1c8617c5452694857ad95c3ee230"

ENV JVM_MINIMUM_MEMORY 512m
ENV JVM_MAXIMUM_MEMORY 4096m

ENV FACTER_BAMBOO_VERSION "6.7.1"
ENV FACTER_BAMBOO_INSTALLDIR "/opt/bamboo"
ENV FACTER_BAMBOO_HOME "/opt/bamboo-home"

ENV FACTER_BAMBOO_CONTEXT ""
ENV FACTER_BAMBOO_PROXY "false"
ENV FACTER_BAMBOO_PROXY_SCHEME "https"
ENV FACTER_BAMBOO_PROXY_NAME "bamboo.local"
ENV FACTER_BAMBOO_PROXY_PORT "443"

ENV FACTER_PRE_RUN_CMD ""
ENV FACTER_EXTRA_PACKS ""

# Puppet stuff all the instalation is donne by puppet
# Just after it we clean up everthing so the end image isn't too big
RUN mkdir /etc/puppet; mkdir /etc/puppet/manifests ; mkdir /etc/puppet/modules
COPY manifests /etc/puppet/manifests/
COPY modules /etc/puppet/modules/
COPY start-service.sh /usr/bin/start-service
RUN chmod +x /usr/bin/start-service ; /opt/puppetlabs/puppet/bin/puppet apply  --modulepath=/etc/puppet/modules /etc/puppet/manifests/base.pp  ;\
 yum clean all ; rm -rf /tmp/* ; rm -rf /var/cache/* ; rm -rf /var/tmp/* ; rm -rf /var/opt/staging

# Ports Bamboo web interface, Bamboo broker
EXPOSE 8085/tcp 54663/tcp

WORKDIR $FACTER_BAMBOO_INSTALLDIR

# Configurations folder, install dir
VOLUME  $FACTER_BAMBOO_HOME


#CMD /opt/puppetlabs/puppet/bin/puppet apply -l /tmp/puppet.log  --modulepath=/etc/puppet/modules /etc/puppet/manifests/start.pp
CMD ["start-service"]
