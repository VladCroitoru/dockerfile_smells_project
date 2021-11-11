FROM adoptopenjdk/maven-openjdk11:latest AS MAVEN_BUILD

COPY pom.xml /build/
COPY src /build/src/

WORKDIR /build/
RUN mvn package

FROM adoptopenjdk:11-jre-hotspot

WORKDIR /app

COPY --from=MAVEN_BUILD /build/target/route-finder-*.jar /app/route-finder.jar

ENTRYPOINT ["java", "-jar", "route-finder.jar"]