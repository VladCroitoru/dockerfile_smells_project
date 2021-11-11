FROM sonarqube:7.9.4-community

USER root

RUN apt-get update -y && apt-get install wget -y
COPY resources/healthcheck /usr/local/bin/

USER sonarqube

RUN mkdir /opt/sonarqube/backup

COPY plugins/ /opt/sonarqube/extensions/plugins/
COPY plugins/ /opt/sonarqube/lib/common/

HEALTHCHECK CMD ["healthcheck"]
