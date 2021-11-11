FROM maven:3
MAINTAINER Shane St Clair<shane@axds.co>

RUN mkdir -p /tmp/mvn_repo

WORKDIR /usr/local/src

ADD pom.xml /usr/local/src

#Download all currently resolvable dependencies (override default local repo, defined as volume upstream)
RUN mvn -Dmaven.repo.local=/tmp/mvn_repo dependency:go-offline

ADD . /usr/local/src
RUN mvn -Dmaven.repo.local=/tmp/mvn_repo clean package \
    && rm -rf /tmp/mvn_repo \
    && mkdir -p /srv/sos-injector-db \
    && mv target/sos-injector-db-*-shaded.jar /srv/sos-injector-db/sos-injector-db.jar \
    && rm -rf /usr/local/src/*

#Add sensor user
RUN useradd --system --home-dir=/srv/sos-injector-db sensor \
      && chown -R sensor:sensor /srv/sos-injector-db

#Run as sensor user
USER sensor

ENTRYPOINT ["java", "-jar", "/srv/sos-injector-db/sos-injector-db.jar"]
