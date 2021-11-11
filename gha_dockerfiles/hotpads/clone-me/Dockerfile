FROM maven:3.6.3-jdk-13 as maven_builder
WORKDIR /app
ADD . /app
RUN ["mvn","clean","install","-T","2C","-DskipTests=true"]

FROM tomcat:9.0.31-jdk13-openjdk-oracle
COPY --from=maven_builder /app/target/clone-me.war /usr/local/tomcat/webapps
