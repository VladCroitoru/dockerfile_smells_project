FROM openjdk:8-jdk-alpine

RUN apk add --update curl tar bash

ARG MAVEN_VERSION=3.3.9

RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
  && curl -fsSL http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz \
    | tar -xzC /usr/share/maven --strip-components=1 \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven

CMD ["mvn"]

RUN apk add --update nodejs && rm -rf /var/cache/apk/*

CMD  ["node"]
CMD  ["npm"]