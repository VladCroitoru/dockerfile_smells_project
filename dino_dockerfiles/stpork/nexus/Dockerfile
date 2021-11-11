FROM openjdk:8-jre-alpine

MAINTAINER stpork from Mordor team

ENV NEXUS_VERSION=3.7.1-02 \
SONATYPE_DIR=/opt/sonatype \
NEXUS_DATA=/nexus-data \
JAVA_MAX_MEM=1200m \
JAVA_MIN_MEM=1200m \
EXTRA_JAVA_OPTS="" 

#CROWD_SERVER=http://jira:8080 \
#CROWD_APPLICATION=nexus \
#CROWD_PASSWORD=nexus-pass

ENV NEXUS_HOME=${SONATYPE_DIR}/nexus

RUN set -x \
&& apk update -qq \
&& update-ca-certificates \
&& apk add --no-cache ca-certificates curl openssl tini \
&& rm -rf /var/cache/apk/* /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/* \
&& mkdir -p ${NEXUS_HOME} ${NEXUS_DATA}/etc ${NEXUS_DATA}/log ${NEXUS_DATA}/tmp ${SONATYPE_DIR}/sonatype-work \
&& curl -fsSL \
"https://download.sonatype.com/nexus/3/nexus-${NEXUS_VERSION}-unix.tar.gz" \
| tar -xz --strip-components=1 -C "${NEXUS_HOME}" \
&& rm -rf ${NEXUS_HOME}/nexus3 \
&& adduser -S -u 1001 -D -H -h ${NEXUS_DATA} -s /bin/false nexus nexus \
&& ln -s ${NEXUS_DATA} ${SONATYPE_DIR}/sonatype-work/nexus3 \
&& chown -R 1001:0 ${NEXUS_HOME} \
&& chown -R 1001:0 ${NEXUS_DATA}

#&& PLUGIN_VERSION=3.2.7 \
#&& PLUGIN_NAME=nexus3-crowd-plugin-${PLUGIN_VERSION} \
#&& curl -fsSL \
#"https://github.com/pingunaut/nexus3-crowd-plugin/releases/download/${PLUGIN_NAME}/${PLUGIN_NAME}.jar" \
#-o ${NEXUS_HOME}/system/${PLUGIN_NAME}.jar \
#&& echo reference\\:file\\:${PLUGIN_NAME}.jar = 200 >> ${NEXUS_HOME}/etc/karaf/startup.properties \
#&& CROWD_PROPS=${NEXUS_HOME}/etc/crowd.properties \
#&& echo crowd.server.url=$CROWD_SERVER >> ${CROWD_PROPS} \
#&& echo application.name=$CROWD_APPLICATION >> ${CROWD_PROPS} \
#&& echo application.password=$CROWD_PASSWORD >> ${CROWD_PROPS} \
#&& echo cache.authentication=false >> ${CROWD_PROPS} \

USER 1001

EXPOSE 8081

VOLUME ${NEXUS_DATA}

WORKDIR ${NEXUS_HOME}

CMD ["/opt/sonatype/nexus/bin/nexus", "run"]

ENTRYPOINT ["/sbin/tini", "--"]
