FROM fedora:24
MAINTAINER Michal Karm Babacek <karm@email.cz>
LABEL description="Tomcat mod_cluster worker example"

ENV DEPS            java-1.8.0-openjdk-devel.x86_64 unzip wget sed tomcat-native
ENV JAVA_HOME       "/usr/lib/jvm/java-1.8.0"

# Tomcat versions
ENV TOMCAT_MAJOR    8
ENV TOMCAT_MINOR    0
ENV TOMCAT_MICRO    36
ENV TOMCAT_VERSION  ${TOMCAT_MAJOR}.${TOMCAT_MINOR}.${TOMCAT_MICRO}
ENV CATALINA_HOME   "/opt/worker/apache-tomcat-${TOMCAT_VERSION}"
ENV TOMCAT_ZIP "http://www-us.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.zip"

# mod_cluster sources
ENV MOD_CLUSTER_GITTAG master
ENV MOD_CLUSTER_REPO   "https://github.com/modcluster/mod_cluster/archive/${MOD_CLUSTER_GITTAG}.zip"

# Apache Maven 3x
ENV MAVEN_VERSION 3.3.9
ENV MAVEN_ZIP     "http://www-us.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.zip"


# Update and configure system
RUN dnf -y update && dnf -y install ${DEPS} && dnf clean all
RUN useradd -s /sbin/nologin worker
RUN mkdir -p /opt/worker && chown worker /opt/worker && chgrp worker /opt/worker && chmod ug+rwxs /opt/worker

WORKDIR /opt/worker
USER worker


# Tomcat installation
RUN wget ${TOMCAT_ZIP} && unzip apache-tomcat-${TOMCAT_VERSION}.zip && rm -rf apache-tomcat-${TOMCAT_VERSION}.zip && \
    chmod ugo+rx ${CATALINA_HOME}/bin/catalina.sh && \
# Apache Maven
    wget ${MAVEN_ZIP} && unzip apache-maven-${MAVEN_VERSION}-bin.zip && rm -rf apache-maven-${MAVEN_VERSION}-bin.zip && \
# mod_cluster
    wget ${MOD_CLUSTER_REPO} && unzip ${MOD_CLUSTER_GITTAG}.zip && rm -rf ${MOD_CLUSTER_GITTAG}.zip && \
    cd mod_cluster-${MOD_CLUSTER_GITTAG} && \
                                                           # TODO: Won't work with Tomcat 8.5
      /opt/worker/apache-maven-${MAVEN_VERSION}/bin/mvn -P TC${TOMCAT_MAJOR} package -DskipTests && \
      for f in `find \( -name "*.jar" -a ! -name "*sources*" -a ! -name "*tests*" \)`; do cp -v $f ${CATALINA_HOME}/lib/; done && \
      cp -v `find ~/ -name "*jboss-logging*Final.jar" | head -n1` ${CATALINA_HOME}/lib/ && \
# cleanup
    rm -rf /opt/worker/mod_cluster-* /opt/worker/apache-maven* ~/.m2

ADD server.xml ${CATALINA_HOME}/conf/server.xml

# main ajp connector
EXPOSE 8009/tcp

ADD worker.sh /opt/worker/
CMD ["/opt/worker/worker.sh"]

