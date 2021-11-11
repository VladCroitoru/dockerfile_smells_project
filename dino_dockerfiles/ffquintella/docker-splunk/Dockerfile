FROM ffquintella/docker-puppet:8.7.2

MAINTAINER Felipe Quintella <docker-puppet@felipe.quintella.email>

#https://www.splunk.com/bin/splunk/DownloadActivityServlet?architecture=x86_64&platform=linux&version=7.2.4.2&product=splunk&filename=splunk-7.2.4.2-fb30470262e3-Linux-x86_64.tgz&wget=true
#https://www.splunk.com/bin/splunk/DownloadActivityServlet?architecture=x86_64&platform=linux&version=7.2.4.2&product=splunk&filename=splunk-7.2.4.2-fb30470262e3-linux-2.6-x86_64.rpm&wget=true

LABEL version="8.1.2.1"
LABEL description="This image contais the splunk application to be used \
as a server."

ENV SPLUNK_PRODUCT splunk enterprise
ENV SPLUNK_VERSION 8.1.2
ENV SPLUNK_BUILD 545206cc9f70
ENV SPLUNK_FILENAME splunk-${SPLUNK_VERSION}-${SPLUNK_BUILD}-linux-2.6-x86_64.rpm

ENV SPLUNK_HOME /opt/splunk
ENV SPLUNK_GROUP splunk
ENV SPLUNK_USER splunk
ENV SPLUNK_BACKUP_DEFAULT_ETC /var/opt/splunk
ENV SPLUNK_OPTIMISTIC_ABOUT_FILE_LOCKING 0

# Users needed by the system
RUN groupadd -g 1000 splunk; adduser --system -u 1000  -g 1000 splunk

# Puppet stuff all the instalation is donne by puppet

ENV FACTER_SPLUNK_VERSION $SPLUNK_VERSION
ENV FACTER_SPLUNK_FILENAME $SPLUNK_FILENAME
ENV FACTER_SPLUNK_HOME $SPLUNK_HOME
ENV FACTER_SPLUNK_GROUP $SPLUNK_GROUP
ENV FACTER_SPLUNK_USER $SPLUNK_USER
ENV FACTER_SPLUNK_BACKUP_DEFAULT_ETC $SPLUNK_BACKUP_DEFAULT_ETC
ENV FACTER_SPLUNK_OPTIMISTIC_ABOUT_FILE_LOCKING $SPLUNK_OPTIMISTIC_ABOUT_FILE_LOCKING

RUN mkdir /etc/puppet; mkdir /etc/puppet/manifests
COPY manifests/base.pp /etc/puppet/manifests/
# Just after it we clean up everthing so the end image isn't too big
RUN /opt/puppetlabs/puppet/bin/puppet apply  /etc/puppet/manifests/base.pp ;\
 yum clean all ; rm -rf /tmp/* ; rm -rf /var/cache/* ; rm -rf /var/tmp/*; mkdir /home/splunk; chown splunk:splunk /home/splunk

# Ports Splunk Web, Splunk Daemon, KVStore, Splunk Indexing Port, Network Input, HTTP Event Collector
EXPOSE 8000/tcp 8089/tcp 8191/tcp 9997/tcp 1514/tcp 1514/udp 8088/tcp 8080/tcp 8080/udp 9887/tcp 9887/udp 514/udp 

WORKDIR /opt/splunk

# Configurations folder, var folder for everyting (indexes, logs, kvstore)
VOLUME [ "/opt/splunk/etc", "/opt/splunk/var" ]

COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod +x /sbin/entrypoint.sh

# Ports Splunk Web, Splunk Daemon, KVStore, Splunk Indexing Port, Network Input, HTTP Event Collector
EXPOSE 8000/tcp 8089/tcp 8191/tcp 9997/tcp 1514 8088/tcp

ENTRYPOINT ["/sbin/entrypoint.sh"]
CMD ["start-service"]
