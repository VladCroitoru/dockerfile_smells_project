FROM adoptopenjdk/openjdk11:jre-11.0.13_8-alpine

RUN apk add --update py-pip
RUN pip install --upgrade pip && pip install -U setuptools && pip install -U pylint
ENV SONAR_SCANNER_VERSION=4.6.2.2472

ADD https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip ./package.zip

RUN unzip package.zip && mv ./sonar-scanner* ./sonar-scanner

ADD entrypoint.sh .
RUN chmod +x /entrypoint.sh

ENV SONAR_SCANNER_OPTS="-Xmx512m"
ENV SONAR_SOURCES="."

WORKDIR /src
ENTRYPOINT [ "/entrypoint.sh" ]
