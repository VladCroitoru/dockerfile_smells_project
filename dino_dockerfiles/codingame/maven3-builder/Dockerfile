FROM techio/java-compiler:1.4

MAINTAINER CodinGame <coders@codingame.com>

ARG MAVEN_VERSION=3.3.9
ARG USER_HOME_DIR="/root"

# Install maven
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
  && curl -fsSL http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz \
    | tar -xzC /usr/share/maven --strip-components=1 \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"

COPY settings.xml $USER_HOME_DIR/.m2/

COPY ./build.sh /project/build
COPY ./docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

