FROM maven:3.6.0-jdk-11 AS build
LABEL maintainer="gs-w_eto_eb_federal_employees@usgs.gov"

# Add pom.xml and install dependencies
COPY pom.xml /build/pom.xml
WORKDIR /build
RUN mvn -B dependency:go-offline

# Add source code and (by default) build the jar
COPY src /build/src
RUN mvn -B clean package


FROM usgswma/openjdk:debian-stretch-openjdk-11.0.2-89c4dd2d55ba476c77aa8fd5274dcb8a1ef115b7

COPY --chown=1000:1000 --from=build /build/target/wqp-etl-nwis-*.jar app.jar

USER $USER

CMD ["java", "-Xmx3G", "-server", "-jar", "app.jar"]