FROM openjdk:8-jre-alpine
LABEL "owner"="dperisro@everis.com"
EXPOSE 8081

ADD build/libs/app.jar /opt/app.jar
WORKDIR /opt
RUN sh -c 'touch app.jar'

ENTRYPOINT exec java ${JAVA_OPTS} -jar app.jar