FROM openjdk:8-jdk-alpine

MAINTAINER stpork from Mordor team

ENV OCP_VERSION=v3.7.0 \
OCP_BUILD=7ed6862 \
CLI_VERSION=7.5.0 \
CLI_BUILD=16285777 \
GRADLE_VERSION=4.3.1 \
JMETER_VERSION=3.3 \
MAVEN_VERSION=3.5.2 \
BAMBOO_VERSION=6.3.0 \
BAMBOO_INSTALL=/opt/atlassian/bamboo \
BAMBOO_HOME=/var/atlassian/application-data/bamboo \
RUN_USER=daemon \
RUN_GROUP=daemon \
BAMBOO_HOME=/var/atlassian/application-data/bamboo \
MAVEN_HOME=/usr/local/maven \
GRADLE_HOME=/usr/local/gradle \
JMETER_HOME=/usr/local/jmeter \
MAVEN_SETTINGS_URL="https://bitbucket.org/stpork/bamboo-agent/downloads/settings.xml"

ENV HOME=$BAMBOO_HOME/home \
M2_HOME=$MAVEN_HOME \
PATH=$MAVEN_HOME/bin:$GRADLE_HOME/bin:$JMETER_HOME/bin:$PATH 

ENV JAVA_TOOL_OPTIONS="-Duser.home=${HOME} -Dbamboo.fs.timestamp.precision=1000"

LABEL io.k8s.description="Atlassian Bamboo"
LABEL io.k8s.display-name="Bamboo ${BAMBOO_VERSION}"
LABEL io.openshift.expose-services="8085:http, 54663:tcp"

RUN set -x \
&& apk update -qq \
&& update-ca-certificates \
&& apk add --no-cache ca-certificates curl git openssh bash procps openssl perl ttf-dejavu tini nano \
&& rm -rf /var/cache/apk/* /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/* \
&& mkdir -p ${BAMBOO_INSTALL} \
&& mkdir -p ${BAMBOO_HOME} \
&& mkdir -p ${MAVEN_HOME} \
&& curl -fsSL \
"http://www.nic.funet.fi/pub/mirrors/apache.org/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz" \
| tar -xz --strip-components=1 -C ${MAVEN_HOME} \
&& mkdir -p ${HOME}/.m2 \
&& curl -fsSL \
${MAVEN_SETTINGS_URL} \
-o ${HOME}/.m2/settings.xml \
&& USR_LOCAL_BIN=/usr/local/bin \
&& curl -fsSL \
"http://github.com/openshift/origin/releases/download/${OCP_VERSION}/openshift-origin-client-tools-${OCP_VERSION}-${OCP_BUILD}-linux-64bit.tar.gz" \
| tar -xz --strip-components=1 -C ${USR_LOCAL_BIN} \
&& mkdir -p ${JMETER_HOME} \
&& curl -fsSL \
"http://mirror.stjschools.org/public/apache/jmeter/binaries/apache-jmeter-${JMETER_VERSION}.tgz" \
| tar -xz --strip-components=1 -C ${JMETER_HOME} \
&& cd ${BAMBOO_INSTALL} \
&& curl -fsSL \
"http://bobswift.atlassian.net/wiki/download/attachments/${CLI_BUILD}/atlassian-cli-${CLI_VERSION}-distribution.zip" \
-o atlassian-cli.zip \
&& unzip -q atlassian-cli.zip \
&& mv atlassian-cli-${CLI_VERSION}/* ${USR_LOCAL_BIN} \
&& rm -rf atlassian-cli* \
&& curl -fsSL \
"https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" \
-o gradle.zip \
&& mkdir -p $GRADLE_HOME \
&& unzip -q gradle.zip \
&& mv gradle-${GRADLE_VERSION}/* ${GRADLE_HOME} \
&& rm -rf gradle* \
&& curl -fsSL \
"http://www.atlassian.com/software/bamboo/downloads/binary/atlassian-bamboo-${BAMBOO_VERSION}.tar.gz" \
| tar -xz --strip-components=1 -C ${BAMBOO_INSTALL} \
&& JMETER_PLUGIN=atlassian-bamboo-jmeter-aggregator-5.14.0.jar \
&& curl -fsSL \
"https://marketplace-cdn.atlassian.com/files/artifact/c89b23ee-76d4-4237-b637-24692f8fb694/${JMETER_PLUGIN}" \
-o ${BAMBOO_INSTALL}/atlassian-bamboo/WEB-INF/lib/${JMETER_PLUGIN} \
&& echo -e "\nbamboo.home=$BAMBOO_HOME" >> "${BAMBOO_INSTALL}/atlassian-bamboo/WEB-INF/classes/bamboo-init.properties" \
&& mkdir /lib64 \
&& ln -s /lib/ld-musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 \
&& chown -R ${RUN_USER}:${RUN_GROUP} ${BAMBOO_INSTALL} \
&& chmod -R 777 ${BAMBOO_INSTALL} \
&& chown -R ${RUN_USER}:${RUN_GROUP} ${BAMBOO_HOME} \
&& chmod -R 777 ${BAMBOO_HOME} \
&& chmod -R 755 ${USR_LOCAL_BIN}

USER ${RUN_USER}:${RUN_GROUP}

EXPOSE 8085
EXPOSE 54663

VOLUME ["${BAMBOO_HOME}"]

WORKDIR ${BAMBOO_HOME}

COPY entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh", "-fg"]
ENTRYPOINT ["/sbin/tini", "--"]
