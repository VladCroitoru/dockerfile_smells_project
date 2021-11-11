FROM centos:7
MAINTAINER Willem van Asperen

ENV DRUID_HOME /opt/druid

# core OS dependencies and configuration
RUN yum -y update \
    && yum -y install \
      java-1.8.0-openjdk

RUN rm /etc/localtime && \
    ln -s /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime && \
    localedef --quiet -c -i en_US -f UTF-8 en_US.UTF-8

# user
RUN mkdir /opt/druid \
    && useradd -ms /bin/bash -d ${DRUID_HOME} druid 

ADD entrypoint.sh ${DRUID_HOME}/entrypoint.sh

# install druid
RUN cd /tmp \
    && curl -O http://static.druid.io/artifacts/releases/druid-0.9.2-bin.tar.gz \
    && tar xzf druid-0.9.2-bin.tar.gz \
    && mv druid-0.9.2 ${DRUID_HOME} \
    && ln -s ${DRUID_HOME}/druid-0.9.2 ${DRUID_HOME}/current \
    && chmod +x ${DRUID_HOME}/entrypoint.sh \
    && chown druid: -R ${DRUID_HOME}

RUN cd /tmp\
    && curl -O http://static.druid.io/artifacts/releases/mysql-metadata-storage-0.9.2.tar.gz \
    && tar xzf mysql-metadata-storage-0.9.2.tar.gz \
    && mv mysql-metadata-storage ${DRUID_HOME}/current/extensions

RUN mkdir ${DRUID_HOME}/current/var \
    && chown -R druid: ${DRUID_HOME}/current/var

VOLUME ${DRUID_HOME}/current/var

ADD common.runtime.properties /opt/druid/current/conf/druid/_common
ADD quickstart/tranquility-server.json /opt/druid/current/conf/tranquility-server.json

EXPOSE 8081 8082 8083 8084 8088 8090 8091 8100-8199 8200

USER druid
WORKDIR ${DRUID_HOME}/current
ENTRYPOINT ["../entrypoint.sh"]
