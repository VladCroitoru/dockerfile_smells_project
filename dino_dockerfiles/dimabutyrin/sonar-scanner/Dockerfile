FROM openjdk:jre-alpine
MAINTAINER Dimitry Butyrin <dimitri.butyrin@brain-agency.com>

ENV SONAR_SCANNER_VERSION 2.8

ADD "https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-${SONAR_SCANNER_VERSION}.zip" /
RUN unzip "sonar-scanner-${SONAR_SCANNER_VERSION}.zip"

ENV PATH "/sonar-scanner-${SONAR_SCANNER_VERSION}/bin:${PATH}"

ENTRYPOINT ["sonar-scanner"]

CMD ["--help"]
