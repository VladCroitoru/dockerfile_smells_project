# QRcode-factory's Dockerfile ==================================================

# DEFINE IMAGE =================================================================
FROM maven:3-jdk-8
MAINTAINER Nicolas Mauger <https://maugern.fr>

# BEFORE INSTALL ===============================================================
ENV LANG en_US.UTF-8

# CONFIGURE MAVEN ==============================================================
COPY pom.xml /srv/QRcode-factory/
WORKDIR /srv/QRcode-factory/

# WEB SERVICE CONFIGURATION ====================================================
COPY src /srv/QRcode-factory/src/
EXPOSE 8080

# START THE WEB SERVER =========================================================
CMD mvn jetty:run -B
