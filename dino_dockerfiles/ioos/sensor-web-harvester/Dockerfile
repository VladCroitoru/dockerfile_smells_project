FROM maven:3
MAINTAINER Shane St Clair<shane@axds.co>

WORKDIR /usr/local/src

ADD pom.xml /usr/local/src/pom.xml
ADD sensor-web-harvester-app/pom.xml /usr/local/src/sensor-web-harvester-app/pom.xml
ADD sensor-web-harvester-iso/pom.xml /usr/local/src/sensor-web-harvester-iso/pom.xml
ADD sensor-web-harvester-main/pom.xml /usr/local/src/sensor-web-harvester-main/pom.xml
ADD sensor-web-harvester-source/pom.xml /usr/local/src/sensor-web-harvester-source/pom.xml
RUN mvn -Dmaven.repo.local=/tmp/mvn_repo dependency:go-offline

#download scala deps
RUN mvn -Dmaven.repo.local=/tmp/mvn_repo dependency:go-offline scala:help

ADD . /usr/local/src

#replace stock log properties with console only docker version
RUN cp docker/log4j.properties /usr/local/src/sensor-web-harvester-app/src/main/resources/log4j.properties

RUN mvn -Dmaven.repo.local=/tmp/mvn_repo clean package \
    && mkdir -p /srv/sensor-web-harvester \
    && mv sensor-web-harvester-app/target/sensor-web-harvester-*.jar /srv/sensor-web-harvester/sensor-web-harvester.jar \
    && rm -rf /usr/local/src/* \
    && rm -rf /tmp/mvn_repo

WORKDIR /srv/sensor-web-harvester

#create directory for database
RUN mkdir -p /srv/swhdb

#Add sensor user
RUN useradd --system --home-dir=/srv/sensor-web-harvester sensor \
      && chown -R sensor:sensor /srv/sensor-web-harvester /srv/swhdb

#Run as sensor user
USER sensor

ENTRYPOINT ["java", "-jar", "/srv/sensor-web-harvester/sensor-web-harvester.jar"]
