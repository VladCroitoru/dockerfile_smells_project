FROM            centos:centos7

MAINTAINER      Alex Tilcock <atilcock@luxoft.com>

ENV             DIST_MIRROR             http://mirror.cc.columbia.edu/pub/software/apache/nifi
ENV             NIFI_HOME               /opt/nifi
ENV             VERSION                 1.0.0
ENV             DISABLE_SSL             true
ENV             DISABLE_LDAP            true

# Install necessary packages, create target directory, download and extract, and update the banner to let people know what version they are using
RUN             yum install -y java-1.8.0-openjdk tar && \
                mkdir -p /opt/nifi && \
                curl ${DIST_MIRROR}/${VERSION}/nifi-${VERSION}-bin.tar.gz | tar xvz -C ${NIFI_HOME} --strip-components=1 && \
                sed -i -e "s|^nifi.ui.banner.text=.*$|nifi.ui.banner.text=Docker NiFi ${VERSION}|" ${NIFI_HOME}/conf/nifi.properties

# Expose web port
EXPOSE          80 443
VOLUME          ["/opt/certs","/opt/sh", "${NIFI_HOME}/flowfile_repository", "${NIFI_HOME}/database_repository", "${NIFI_HOME}/content_repository", "${NIFI_HOME}/provenance_repository"]

ADD             ./start.sh /opt/sh/
RUN             chmod +x /opt/sh/start.sh
CMD             ["/opt/sh/start.sh"]
