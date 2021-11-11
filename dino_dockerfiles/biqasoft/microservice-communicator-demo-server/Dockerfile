FROM java:openjdk-8u91-jdk
VOLUME /tmp

ENV MAVEN_VERSION 3.3.9
ENV HOME /root

RUN mkdir -p /usr/share/maven \
  && curl -fsSL http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz \
    | tar -xzC /usr/share/maven --strip-components=1 \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven

RUN apt-get update
ADD . /tmp
RUN cd /tmp && mvn package && mv target/release.jar /app.jar

EXPOSE 8080
RUN bash -c 'touch /app.jar'
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom", "-jar", "/app.jar"]