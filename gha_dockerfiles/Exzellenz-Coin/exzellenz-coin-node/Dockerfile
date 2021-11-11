FROM maven:3.6.3-openjdk-16 AS MAVEN_TOOL_CHAIN
COPY pom.xml /tmp/
COPY src /tmp/src/
WORKDIR /tmp/
RUN mvn -T 4C install
RUN rm /tmp/target/ExcellenceCoinNode-*-sources.jar

FROM openjdk:16-alpine
WORKDIR /app
COPY --from=MAVEN_TOOL_CHAIN /tmp/target/ExcellenceCoinNode-*.jar app.jar
RUN mkdir /data
EXPOSE 1337
CMD java --add-opens java.base/java.math=ALL-UNNAMED -jar /app/app.jar
