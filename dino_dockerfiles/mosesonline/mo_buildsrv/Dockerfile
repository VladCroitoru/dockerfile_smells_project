FROM mosesonline/mo_jenkins:2.67

ARG MAVEN_VERSION
ENV MAVEN_VERSION ${MAVEN_VERSION:-3.5.0}
ENV MAVEN_SHA ${MAVEN_SHA:-878b8b93a8f9685aefba5c21a17b46eb141b1122}
ENV MAVEN_HOME /opt/maven

USER root
RUN curl -fsSL http://www-us.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz -o /tmp/apache-maven-$MAVEN_VERSION-bin.tar.gz \
    && echo "$MAVEN_SHA /tmp/apache-maven-$MAVEN_VERSION-bin.tar.gz" | sha1sum -c - \
    && mkdir $MAVEN_HOME && tar -xzf /tmp/apache-maven-$MAVEN_VERSION-bin.tar.gz --strip-components=1 -C $MAVEN_HOME
VOLUME /opt/maven/conf
USER jenkins