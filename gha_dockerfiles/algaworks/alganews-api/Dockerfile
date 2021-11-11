# Build
FROM maven:3-openjdk-11 as target
WORKDIR /build
COPY pom.xml .
RUN mvn dependency:go-offline

COPY src/ /build/src/
RUN mvn package

# Run
FROM openjdk:11-jre
EXPOSE 8080
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
CMD exec java $JAVA_OPTS -Xverify:none -XX:TieredStopAtLevel=1 -jar /app.jar
COPY --from=target /build/target/alganews-api-0.0.1-SNAPSHOT.jar /app.jar