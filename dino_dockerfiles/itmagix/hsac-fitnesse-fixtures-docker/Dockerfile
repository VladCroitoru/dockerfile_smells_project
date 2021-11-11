FROM maven:3.5.3-jdk-8-alpine
MAINTAINER Maikel Dollé <maikel@itmagix.nl>
RUN apk update && \
    apk add git
ENV HSACVER=1.3.0
ENV FNROOT=/opt/fitnesse
WORKDIR $FNROOT
RUN git clone https://github.com/fhoeben/hsac-fitnesse-fixtures.git && \
    cd hsac-fitnesse-fixtures && \
    mvn clean package -DskipTests
ENTRYPOINT ["java", "-jar", "/opt/fitnesse/hsac-fitnesse-fixtures/wiki/fitnesse-standalone.jar", "-r", "hsac-fitnesse-fixtures/wiki/FitNesseRoot"]
