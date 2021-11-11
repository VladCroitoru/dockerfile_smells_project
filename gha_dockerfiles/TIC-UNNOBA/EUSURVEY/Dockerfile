#FROM maven:3.8.2-openjdk-11 as build
#WORKDIR /
#COPY pom.xml /
#COPY src /src
#RUN mvn clean install -DskipTests=true -Denvironment=oss

FROM tomcat:8.5.41-jdk8
#FROM tomcat:8.5.2-jre8
# arguments
# ./conf/eulogin.crt is a trusted certificate for SSO integration
# ./conf/context.xml is the context configuration for tomcat
# ./conf/manager-context.xml is the tomcat's manager context configuration
# ./conf/setenv.sh is the environment variables configuration

#COPY ./conf/eulogin.crt eulogin.crt

#RUN echo yes | keytool -importcert -alias euloginCertAlias -storepass changeit -file eulogin.crt -keystore "$JAVA_HOME/jre/lib/security/cacerts"

RUN ["rm", "-fr", "/usr/local/tomcat/webapps/ROOT"]
COPY /target/eusurvey.war /usr/local/tomcat/webapps/eusurvey.war
COPY eusurvey.war /usr/local/tomcat/webapps/eusurvey.war
COPY ./docker/server/conf/setenv.sh /usr/local/tomcat/bin/setenv.sh
COPY ./docker/server/conf/context.xml /usr/local/tomcat/conf/context.xml
COPY ./docker/server/conf/manager-context.xml /usr/local/tomcat/webapps/manager/META-INF/context.xml
