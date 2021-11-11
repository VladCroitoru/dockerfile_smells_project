FROM openjdk:8-jre-alpine
WORKDIR /opt/docker
ADD target/docker/stage/opt /opt
RUN adduser -D -u 1000 drt-admin

RUN ["chown", "-R", "1000:1000", "."]

RUN apk --update add bash curl ca-certificates

RUN rm -rf /var/cache/apk/*

COPY certs/rds-combined-ca-bundle.der /etc/drt/rds-combined-ca-bundle.der
COPY certs/rds-ca-2019-root.der /etc/drt/rds-ca-2019-root.der

RUN echo keytool $KEYTOOL_PASSWORD
RUN keytool -noprompt -storepass changeit -import -alias rds-root-deprecated -keystore $JAVA_HOME/lib/security/cacerts -file /etc/drt/rds-combined-ca-bundle.der
RUN keytool -noprompt -storepass changeit -import -alias rds-root -keystore $JAVA_HOME/lib/security/cacerts -file /etc/drt/rds-ca-2019-root.der

RUN mkdir -p /var/data/logs
RUN chown 1000:1000 -R /var/data/logs

USER 1000

ENTRYPOINT ["bin/drt-analytics"]
