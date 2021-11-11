FROM maven:3-jdk-11 AS build
COPY settings-docker.xml /usr/share/maven/ref/
COPY src /usr/src/app/src
COPY pom.xml /usr/src/app
RUN mvn -f /usr/src/app/pom.xml -gs /usr/share/maven/ref/settings-docker.xml -Dextract.test.name=Extraction_Pro_sante_connect_cartes_de_test_bascule -DskipTests clean package

FROM openjdk:11-slim-buster
RUN echo "deb [trusted=yes] http://repo.proxy-dev-forge.asip.hst.fluxus.net/artifactory/debian.org buster main" > /etc/apt/sources.list \
    && echo "deb [trusted=yes] http://repo.proxy-dev-forge.asip.hst.fluxus.net/artifactory/debian.org buster-updates main" >> /etc/apt/sources.list \
    && apt update \
    && apt install -y wget gnupg dos2unix \
    && wget -qO - http://repo.proxy-dev-forge.asip.hst.fluxus.net/artifactory/www.mongodb.org/static/pgp/server-5.0.asc | apt-key add - \
    && echo "deb [trusted=yes] http://repo.proxy-dev-forge.asip.hst.fluxus.net/artifactory/debian-repo.mongodb.org buster/mongodb-org/5.0 main" | tee /etc/apt/sources.list.d/mongodb-org-5.0.list
RUN apt update
RUN apt install -y mongodb-database-tools mongodb-mongosh
COPY --from=build /usr/src/app/target/pscextract-*.jar /usr/app/pscextract.jar
RUN mkdir -p /app/extract-repo && mkdir -p /app/resources
COPY --from=build /usr/src/app/src/main/resources/aggregate.mongo /app/resources/
RUN chown -R daemon: /app
USER daemon
EXPOSE 8080
ENTRYPOINT ["java","-jar","/usr/app/pscextract.jar"]
