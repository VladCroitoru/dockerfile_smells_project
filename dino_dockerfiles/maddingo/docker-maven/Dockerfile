FROM jenkins/jnlp-slave

ENV MAVEN_VERSION=3.5.2
ENV MAVEN_SHA1=190dcebb8a080f983af4420cac4f3ece7a47dd64

# Download and install maven
USER root
RUN \
    mkdir -p /usr/share/maven && \
    cd /tmp && \
    curl -O https://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz && \
    sha1sum apache-maven-$MAVEN_VERSION-bin.tar.gz | grep $MAVEN_SHA1 && \
    cd /tmp && tar -xz -f apache-maven-$MAVEN_VERSION-bin.tar.gz -C /usr/share/maven --strip-components=1 && \
    rm /tmp/apache-maven*

# configure maven
RUN \
  ln -s /usr/share/maven/bin/mvn /usr/bin/mvn && \
  echo export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF-8 >/etc/mavenrc

USER jenkins
