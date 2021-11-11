FROM openjdk:8-jdk-alpine as builder
RUN apk add unzip && rm -rf /var/cache/apk/*
ENV MAVEN_VERSION 3.6.1
ENV MAVEN_HOME /usr/lib/mvn
ENV PATH $MAVEN_HOME/bin:$PATH
RUN wget http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  tar -zxvf apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  rm apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  mv apache-maven-$MAVEN_VERSION /usr/lib/mvn
WORKDIR /app
COPY . .
RUN ls -l
RUN rm -rf ./target && mvn -f pom.xml package && unzip -o ./target/*.jar -d /tmp

# the final deployment image
#FROM openjdk:8-jdk-alpine
FROM quay.io/gatblau/openjdk:14-j9-ubi8-min
MAINTAINER Gatblau <onix@gatblau.org>
LABEL author="gatblau.org"
COPY --from=builder /tmp/BOOT-INF/lib /app/lib
COPY --from=builder /tmp/META-INF /app/META-INF
COPY --from=builder /tmp/BOOT-INF/classes /app
USER 20
ENTRYPOINT ["java","-cp","app:app/lib/*","com/example/sslserver/SslServerApplication"]