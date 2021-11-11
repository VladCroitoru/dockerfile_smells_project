FROM navikt/java:11-appdynamics

ENV APPLICATION_NAME=familie-ba-soknad-api
ENV APPD_ENABLED=TRUE
ENV JAVA_OPTS="-Dhttps.protocols=TLSv1,TLSv1.1,TLSv1.2"

COPY ./target/familie-ba-soknad-api-1.0-SNAPSHOT.jar "app.jar"
