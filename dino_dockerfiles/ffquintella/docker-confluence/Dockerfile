FROM ffquintella/docker-puppet:latest

MAINTAINER Felipe Quintella <docker-jira@felipe.quintella.email>

LABEL version="6.15.4"
LABEL description="This image contais the confluence application to be used \
as a server."


#http://product-downloads.atlassian.com/software/confluence/downloads/atlassian-confluence-6.15.4.tar.gz

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

ENV JAVA_HOME "/opt/java_home/java_home"
ENV CONFLUENCE_VERSION "6.15.4"
ENV CONFLUENCE_INSTALLDIR "/opt/confluence"
ENV CONFLUENCE_HOME "/opt/confluence-home"


ENV FACTER_CONFLUENCE_VERSION $CONFLUENCE_VERSION
ENV FACTER_CONFLUENCE_INSTALLDIR $CONFLUENCE_INSTALLDIR
ENV FACTER_CONFLUENCE_HOME $CONFLUENCE_HOME

ENV FACTER_JAVA_HOME "/opt/java_home"
ENV FACTER_JAVA_VERSION "8"
ENV FACTER_JAVA_VERSION_UPDATE "212"
ENV FACTER_JAVA_VERSION_BUILD "04"
ENV FACTER_JAVA_VERSION_HASH "59066701cf1a433da9770636fbc4c9aa"

ENV JVM_MINIMUM_MEMORY 1024m
ENV JVM_MAXIMUM_MEMORY 6144m


ENV FACTER_PRE_RUN_CMD ""
ENV FACTER_EXTRA_PACKS ""

# Puppet stuff all the instalation is donne by puppet
# Just after it we clean up everthing so the end image isn't too big
RUN mkdir /etc/puppet; mkdir /etc/puppet/manifests ; mkdir /etc/puppet/modules ; mkdir /opt/scripts
COPY manifests /etc/puppet/manifests/
COPY modules /etc/puppet/modules/
COPY start-service.sh /opt/scripts/start-service.sh
RUN chmod +x /opt/scripts/start-service.sh ; ln -s /opt/scripts/start-service.sh /usr/bin/start-service ;/opt/puppetlabs/puppet/bin/puppet apply  --modulepath=/etc/puppet/modules /etc/puppet/manifests/base.pp  ;\
 yum clean all ; rm -rf /tmp/* ; rm -rf /var/cache/* ; rm -rf /var/tmp/* ; rm -rf /var/opt/staging

COPY --chown=confluence:confluence setenv.sh ${CONFLUENCE_INSTALLDIR}/atlassian-confluence-${CONFLUENCE_VERSION}/bin
COPY --chown=confluence:confluence user.sh ${CONFLUENCE_INSTALLDIR}/atlassian-confluence-${CONFLUENCE_VERSION}/bin

RUN chmod +x ${CONFLUENCE_INSTALLDIR}/atlassian-confluence-${CONFLUENCE_VERSION}/bin/*

# Ports Jira web interface
EXPOSE 8090/tcp

WORKDIR $FACTER_CONFLUENCE_INSTALLDIR

# Configurations folder, install dir
VOLUME  $CONFLUENCE_HOME

#CMD /opt/puppetlabs/puppet/bin/puppet apply -l /tmp/puppet.log  --modulepath=/etc/puppet/modules /etc/puppet/manifests/start.pp
CMD ["start-service"]
