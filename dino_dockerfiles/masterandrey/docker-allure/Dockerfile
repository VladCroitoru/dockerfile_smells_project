FROM openjdk:8-jre

COPY allure-2.0.1.tgz /

RUN apt-get update \
    && apt-get install tar \
    && tar -xvf allure-2.0.1.tgz \
    && chmod -R +x /allure-2.0.1/bin

VOLUME ["/allure-results"]
VOLUME ["/allure-report"]

WORKDIR /allure-2.0.1/bin
