FROM docker:1.10.3-dind

# JAVA JDK 8
RUN echo "INSTALLING OPENJDK 8..." && \
    apk update && apk upgrade && \
    apk add openjdk8 && \
    mkdir /tmp/tmprt && \
    cd /tmp/tmprt && \
    apk add zip && \
    unzip -q /usr/lib/jvm/default-jvm/jre/lib/rt.jar && \
    apk add zip && \
    zip -q -r /tmp/rt.zip . && \
    apk del zip && \
    cd /tmp && \
    mv rt.zip /usr/lib/jvm/default-jvm/jre/lib/rt.jar && \
    rm -rf /tmp/tmprt /var/cache/apk/* bin/jjs bin/keytool bin/orbd bin/pack200 bin/policytool \
          bin/rmid bin/rmiregistry bin/servertool bin/tnameserv bin/unpack200

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/

# GIT - NODEJS - JQ
RUN echo "INSTALLING GIT AND NODEJS..." \
  && apk add --no-cache git bash openssh nodejs curl tar jq

# MAVEN
RUN echo "INSTALLING MAVEN..."

ARG MAVEN_VERSION=3.3.9
ARG USER_HOME_DIR="/root"

RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
  && curl -fsSL http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz \
    | tar -xzC /usr/share/maven --strip-components=1 \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"

VOLUME "$USER_HOME_DIR/.m2"

# RANCHER-COMPOSE
RUN echo "INSTALLING RANCHER-COMPOSE..." \
  && mkdir -p /usr/share/rancher-compose \
  && curl -fsSL https://github.com/rancher/rancher-compose/releases/download/v0.12.1/rancher-compose-linux-amd64-v0.12.1.tar.gz \
  | tar -xzC /usr/share/rancher-compose --strip-components=2 \
  && ln -s /usr/share/rancher-compose/rancher-compose /usr/bin/rancher-compose
