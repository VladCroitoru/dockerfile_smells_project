### Build using Maven ###
FROM maven:3.6.0-jdk-8-alpine AS maven
ARG profile

COPY pom.xml /tmp/
COPY . /tmp/

WORKDIR /tmp/

## For debugging reasons  ##
RUN if [[ -z "$profile" ]] ; then echo "Building without profile"; sleep 2 ; else echo "Building using profile: '$profile'"; sleep 2 ; fi

## run maven based of profile given ##
RUN if [[ -z "$profile" ]] ; then mvn package -U ; else mvn package -U -P $profile ; fi


### Deploy to Tomcat ###
FROM tomcat:8.5-jre8-alpine
MAINTAINER "spyroukon@gmail.com"
RUN ["rm", "-fr", "/usr/local/tomcat/webapps/ROOT"]

COPY --from=maven /tmp/eic-registry/target/eic-registry.war /usr/local/tomcat/webapps/eic-registry.war
COPY ./eic-registry/src/main/resources/application.properties /usr/local/tomcat/lib/registry.properties
COPY ./eic-registry/server.xml /usr/local/tomcat/conf/server.xml

RUN ["cat", "/usr/local/tomcat/lib/registry.properties"]
CMD ["catalina.sh", "run"]
