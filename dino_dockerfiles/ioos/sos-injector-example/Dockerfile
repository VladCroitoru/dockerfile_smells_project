FROM maven:3
MAINTAINER Shane St Clair<shane@axds.co>

RUN mkdir -p /tmp/mvn_repo

#Add pom for dependency resolution
ADD pom.xml /usr/local/src/sos-injector-example/pom.xml

WORKDIR /usr/local/src/sos-injector-example

#Download all currently resolvable dependencies (override default local repo, defined as volume upstream)
RUN mvn -Dmaven.repo.local=/tmp/mvn_repo dependency:go-offline

#Add project
ADD . /usr/local/src/sos-injector-example

RUN mvn clean -Dmaven.repo.local=/tmp/mvn_repo package \
    && rm -rf /tmp/mvn_repo \
    && mkdir -p /srv/sos-injector-example \
    && mv target/sos-injector-example-*.jar /srv/sos-injector-example/sos-injector-example.jar \
    && rm -rf /usr/local/src/sos-injector-example

WORKDIR /srv/sos-injector-example

#Add sensor user
RUN useradd --system --home-dir=/srv/sos-injector-example sensor \
      && chown -R sensor:sensor /srv/sos-injector-example

#Run as sensor user
USER sensor

ENTRYPOINT ["java", "-jar", "/srv/sos-injector-example/sos-injector-example.jar"]
