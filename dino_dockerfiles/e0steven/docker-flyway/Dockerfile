#
# Flyway image with MySQL Driver
#

FROM alpine

WORKDIR /flyway

ENV FLYWAY_VERSION=4.2.0 MYSQL_DRIVER_VERSION=8.0.15 DOCKERIZE_VERSION=v0.2.0

RUN apk update \
  && apk add --no-cache openjdk8-jre \
  && apk add --update autossh \
  && apk add --no-cache bash \
  && apk add openssl \
  && wget https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/${FLYWAY_VERSION}/flyway-commandline-${FLYWAY_VERSION}.tar.gz \
  && tar -xzf flyway-commandline-${FLYWAY_VERSION}.tar.gz \
  && mv flyway-${FLYWAY_VERSION}/* . \
  && rm flyway-commandline-${FLYWAY_VERSION}.tar.gz \
  && ln -s /flyway/flyway /usr/local/bin/flyway \
  && wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/${MYSQL_DRIVER_VERSION}/mysql-connector-java-${MYSQL_DRIVER_VERSION}.jar \
  && mv mysql-connector-java-${MYSQL_DRIVER_VERSION}.jar drivers \
  && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && echo -ne "- with FlyWay $FLYWAY_VERSION\n" >> /root/.built

CMD ["flyway", "--help"]
EXPOSE 1-65535
