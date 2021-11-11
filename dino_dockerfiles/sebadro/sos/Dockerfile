FROM maven:3.5-jdk-8-alpine as build
WORKDIR /app
COPY . /app/
RUN mvn clean install -DskipTests

FROM tomcat:9-jre8-alpine
COPY --from=build /app/webapp/target/52n-sos-webapp/ $CATALINA_HOME/webapps/52n-sos-webapp
COPY --from=build /app/docker/tomcat-conf/ $CATALINA_HOME/conf/
RUN apk --update add fontconfig ttf-dejavu
ENV JAVA_OPTS="-Djava.awt.headless=true"