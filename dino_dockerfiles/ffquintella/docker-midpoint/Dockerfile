FROM ffquintella/docker-puppet:latest

MAINTAINER Felipe Quintella <docker-jira@felipe.quintella.email>

LABEL version="3.5.1.1"
LABEL description="This image contais the midpoint application"


ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

ENV JAVA_HOME "/opt/java_home/java_home"

ENV MIDPOINT_VERSION "3.5.1"

ENV MIDPOINT_HOME "/var/opt/midpoint"
ENV MIDPOINT_INSTALL_DIR "/opt/midpoint"

ENV TOMCAT_VERSION 8.5.15

ENV JAVA_OPTS "-Xms256m -Xmx2048m -Xss1m -Dmidpoint.home=${MIDPOINT_HOME} -Djavax.net.ssl.trustStore=/var/opt/midpoint/keystore.jceks -Djavax.net.ssl.trustStoreType=jceks"

RUN echo 'JAVA_OPTS="${JAVA_OPTS}"'

ENV FACTER_MIDPOINT_VERSION $MIDPOINT_VERSION
ENV FACTER_RUNDECK_DB_TYPE $RUNDECK_DB_TYPE
ENV FACTER_RUNDECK_URL $RUNDECK_URL

ENV FACTER_JAVA_HOME "/opt/java_home"
ENV FACTER_JAVA_VERSION "8"
ENV FACTER_JAVA_VERSION_UPDATE "131"
ENV FACTER_JAVA_VERSION_BUILD "11"
ENV FACTER_JAVA_VERSION_HASH "d54c1d3a095b4ff2b6607d096fa80163"

ENV FACTER_TOMCAT_HOME "/opt/tomcat"
ENV FACTER_TOMCAT_URL "http://ftp.unicamp.br/pub/apache/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz"

ENV FACTER_MIDPOINT_HOME $MIDPOINT_HOME
ENV FACTER_MIDPOINT_INSTALL_DIR $MIDPOINT_INSTALL_DIR

ENV FACTER_PRE_RUN_CMD ""
ENV FACTER_EXTRA_PACKS ""

# Puppet stuff all the instalation is donne by puppet
# Just after it we clean up everthing so the end image isn't too big
RUN mkdir /etc/puppet; mkdir /etc/puppet/manifests ; mkdir /etc/puppet/modules ; mkdir /opt/scripts
COPY manifests /etc/puppet/manifests/
COPY modules /etc/puppet/modules/
COPY start-service.sh /opt/scripts/start-service.sh
RUN chmod +x /opt/scripts/start-service.sh ; ln -s /opt/scripts/start-service.sh /usr/bin/start-service ;/opt/puppetlabs/puppet/bin/puppet apply -l /tmp/puppet.log  --modulepath=/etc/puppet/modules /etc/puppet/manifests/base.pp  ;\
 yum clean all ; rm -rf /tmp/* ; rm -rf /var/cache/* ; rm -rf /var/tmp/* ; rm -rf /var/opt/staging

# Ports to web interface
EXPOSE 8080/tcp

WORKDIR '/opt'

# Configurations folder, install dir
VOLUME  $MIDPOINT_HOME

#CMD /opt/puppetlabs/puppet/bin/puppet apply -l /tmp/puppet.log  --modulepath=/etc/puppet/modules /etc/puppet/manifests/start.pp
CMD ["start-service"]
