FROM openjdk:8-jdk
ARG PROJ_DIR=/simplespringapp
WORKDIR ${PROJ_DIR}
ADD pom.xml ${PROJ_DIR}/pom.xml
ADD src ${PROJ_DIR}/src
RUN apt-get update && apt-get install -y maven && mvn clean install
CMD ["mvn", "jetty:run"]
