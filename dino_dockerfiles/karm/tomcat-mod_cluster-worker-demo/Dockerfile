FROM karm/tomcat-mod_cluster-worker:latest
MAINTAINER Michal Karm Babacek <karm@email.cz>
LABEL description="Tomcat mod_cluster worker example with a demo application"

ENV CLUSTERBENCH_GITTAG=simplified-and-pure
ENV CLUSTERBENCH_REPO=https://github.com/Karm/clusterbench/archive/${CLUSTERBENCH_GITTAG}.zip

# Apache Maven
RUN wget ${MAVEN_ZIP} && unzip apache-maven-${MAVEN_VERSION}-bin.zip && rm -rf apache-maven-${MAVEN_VERSION}-bin.zip && \
# mod_cluster
    wget ${CLUSTERBENCH_REPO} && unzip ${CLUSTERBENCH_GITTAG}.zip && rm -rf ${CLUSTERBENCH_GITTAG}.zip && \
    cd clusterbench-${CLUSTERBENCH_GITTAG} && \
      /opt/worker/apache-maven-${MAVEN_VERSION}/bin/mvn package -Pee7 -DskipTests && \
      cp -v `find \( -name "*.war" \) | head -n1` ${CATALINA_HOME}/webapps/ && \
# cleanup
    rm -rf /opt/worker/clusterbench* /opt/worker/apache-maven* ~/.m2

