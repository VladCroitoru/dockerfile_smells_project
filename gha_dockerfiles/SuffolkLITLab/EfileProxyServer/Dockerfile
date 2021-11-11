ARG EFM_SUPPORT=tyler

# TODO(brycew): consider http://whichjdk.com/#adoptium-eclipse-temurin
FROM maven:3.8-openjdk-17 AS build_tyler
ONBUILD COPY pom.xml LICENSE client_sign.properties quartz.properties Suffolk.pfx /usr/src/app/

FROM maven:3.8-openjdk-17 AS build_no_tyler
ONBUILD COPY pom.xml LICENSE quartz.properties /usr/src/app/

FROM build_${EFM_SUPPORT}
# Install all of the maven packages, so we don't have to every time we change code
RUN mvn -f /usr/src/app/pom.xml clean dependency:resolve dependency:go-offline test package && mvn -f /usr/src/app/pom.xml test
COPY src /usr/src/app/src
RUN mvn -f /usr/src/app/pom.xml package dependency:build-classpath -Dmdep.outputFile=cp.txt -PnoDockerTests
COPY docker_run_script.sh /usr/src/app

EXPOSE 9000

CMD [ "/bin/sh", "/usr/src/app/docker_run_script.sh" ]
