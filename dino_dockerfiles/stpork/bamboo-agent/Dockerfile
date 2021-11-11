FROM openjdk:8-jdk-alpine

MAINTAINER stpork from Mordor team

ENV LANG=C.UTF-8 \
OCP_VERSION=v3.7.0 \
OCP_BUILD=7ed6862 \
CLI_VERSION=7.5.0 \
CLI_BUILD=16285777 \
GRADLE_VERSION=4.3.1 \
JMETER_VERSION=3.3 \
MAVEN_VERSION=3.5.2 \
BAMBOO_VERSION=6.3.0 \
BAMBOO_INSTALL=/opt/atlassian/bamboo-agent \
BAMBOO_HOME=/var/atlassian/application-data/bamboo \
BAMBOO_SERVER_URL=http://bamboo:8085/agentServer/ \
RUN_USER=daemon \
RUN_GROUP=daemon \
MAVEN_HOME=/usr/local/maven \
GRADLE_HOME=/usr/local/gradle \
JMETER_HOME=/usr/local/jmeter \
MAVEN_SETTINGS_URL="http://artifactory:8081/artifactory/generic-local/cicd/maven/settings.xml"

ENV HOME=$BAMBOO_HOME/home \
M2_HOME=$MAVEN_HOME \
PATH=$MAVEN_HOME/bin:$GRADLE_HOME/bin:$JMETER_HOME/bin:$PATH \
BAMBOO_AGENT_JAR=atlassian-bamboo-agent-installer-${BAMBOO_VERSION}.jar

ENV JAVA_TOOL_OPTIONS="-Duser.home=${HOME} -Dbamboo.fs.timestamp.precision=1000"

LABEL io.k8s.description="Atlassian Bamboo Agent"
LABEL io.k8s.display-name="Bamboo Agent ${BAMBOO_VERSION}"

RUN set -x \
&& ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-glibc/releases/download" \
&& ALPINE_GLIBC_PACKAGE_VERSION="2.26-r0" \
&& ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk" \
&& ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" \
&& ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk" \
&& apk update -qq \
&& update-ca-certificates \
&& apk add --no-cache --virtual=.build-dependencies wget ca-certificates \
&& wget -q \
"https://raw.githubusercontent.com/andyshinn/alpine-pkg-glibc/master/sgerrand.rsa.pub" \
-O "/etc/apk/keys/sgerrand.rsa.pub" \
&& wget -q \
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" \
&& apk add --no-cache \
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" \
&& rm "/etc/apk/keys/sgerrand.rsa.pub" \
&& /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 C.UTF-8 || true \
&& echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh \
&& apk del glibc-i18n \
&& rm -rf "/root/.wget-hsts" \
&& apk del .build-dependencies \
&& rm \
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" \
&& apk add --no-cache ca-certificates wget curl git openssh bash procps openssl perl tini \
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
https://bitbucket.org/stpork/bamboo-agent/downloads/${BAMBOO_AGENT_JAR} \
-o ${BAMBOO_INSTALL}/${BAMBOO_AGENT_JAR} \
&& chown -R ${RUN_USER}:${RUN_GROUP} ${BAMBOO_INSTALL} \
&& chmod -R 777 ${BAMBOO_INSTALL} \
&& chown -R ${RUN_USER}:${RUN_GROUP} ${BAMBOO_HOME} \
&& chmod -R 777 ${BAMBOO_HOME} \
&& chmod -R 755 ${USR_LOCAL_BIN}

USER ${RUN_USER}:${RUN_GROUP}

WORKDIR ${BAMBOO_HOME}

COPY entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]
ENTRYPOINT ["/sbin/tini", "--"]
