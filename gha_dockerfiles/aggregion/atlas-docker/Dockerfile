FROM openjdk:8

ARG VERSION=3.0.0-SNAPSHOT

ENV ATLAS_INSTALL=/opt/install/apache-atlas-${VERSION}
ENV ATLAS_CONF_INSTALL=${ATLAS_INSTALL}/conf
ENV ATLAS_BIN_INSTALL=${ATLAS_INSTALL}/bin
ENV ATLAS_HOME=/opt/apache-atlas-${VERSION}
ENV ATLAS_CONF=/opt/apache-atlas-${VERSION}/conf
ENV ATLAS_BIN=/opt/apache-atlas-${VERSION}/bin
ENV MANAGE_LOCAL_SOLR=false
ENV MANAGE_LOCAL_HBASE=false

# Install python
RUN apt-get update
RUN apt-get install -y python2.7 netcat gettext-base

# Create atlas user
RUN groupadd -r -g 47144 atlas && useradd -r -u 47145 -g atlas atlas

# Add files
ADD https://storage.aggregion.com/api/files/2a3e16a670c5de51130b21a9166566048c3295c4c2ec0b0af585f55685055530/shared/data /tmp/atlas.tar.gz
RUN cd /opt && tar xzf /tmp/atlas.tar.gz && rm -f /tmp/atlas.tar.gz

# Start script
RUN mkdir -p ${ATLAS_HOME}

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ADD configure.sh /configure.sh
RUN chmod +x /configure.sh

ADD atlas-application.properties.template /opt/apache-atlas-${VERSION}/conf/atlas-application.properties.template
ADD models/9000-Aggregion/ /opt/apache-atlas-${VERSION}/models/9000-Aggregion/

RUN ln -s /opt/atlas /opt/apache-atlas-${VERSION}

EXPOSE 21000

WORKDIR ${ATLAS_HOME}

CMD ["/entrypoint.sh"]
