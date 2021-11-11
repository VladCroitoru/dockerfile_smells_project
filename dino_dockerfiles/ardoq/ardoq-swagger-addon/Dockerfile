FROM ardoq/leiningen-jre:11.0.12_7-2.9.4
MAINTAINER Kristian Helgesen "kristian@ardoq.com"

ENV VERSION 1.0.22
ENV LEIN_ROOT disable
ENV API_BASE_URL https://app.ardoq.com
ENV PORT 8080

RUN adduser --disabled-login --disabled-password -u 50000 ardoq
USER ardoq

COPY ./target/ardoq-swagger-addon-$VERSION-standalone.jar /usr/src/app/app-standalone.jar

EXPOSE 8080
WORKDIR /usr/src/app
CMD ["java", "-jar", "app-standalone.jar"]
