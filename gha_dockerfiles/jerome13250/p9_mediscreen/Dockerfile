## This uses multi-stage build :
## https://docs.docker.com/develop/develop-images/multistage-build/

## Need to add curl to the alpine for healthcheck in docker-compose.yml file

###########################
#microservice mpatient
###########################
# Alpine Linux with OpenJDK JRE
FROM openjdk:8-jre-alpine AS mpatient
# Add folder :
RUN mkdir /tmp/app
# copy JAR into image
COPY ./mpatient/target/mpatient-0.0.1-SNAPSHOT.jar /tmp/app
#api port
EXPOSE 8081
# run java app:
CMD java -jar /tmp/app/mpatient-0.0.1-SNAPSHOT.jar

###########################
#microservice mnote
###########################
# Alpine Linux with OpenJDK JRE
FROM openjdk:8-jre-alpine AS mnote
# Add folder :
RUN mkdir /tmp/app
# copy JAR into image
COPY ./mnote/target/mnote-0.0.1-SNAPSHOT.jar /tmp/app
#api port
EXPOSE 8082
# run java app:
CMD java -jar /tmp/app/mnote-0.0.1-SNAPSHOT.jar

###############################
#microservice mdiabeteassess
###############################
# Alpine Linux with OpenJDK JRE
FROM openjdk:8-jre-alpine AS mdiabeteassess
# Add folder :
RUN mkdir /tmp/app
# copy JAR into image
COPY ./mdiabeteassess/target/mdiabeteassess-0.0.1-SNAPSHOT.jar /tmp/app
#api port
EXPOSE 8083
# run java app:
CMD java -jar /tmp/app/mdiabeteassess-0.0.1-SNAPSHOT.jar

###########################
#Client UI
###########################
# Alpine Linux with OpenJDK JRE
FROM openjdk:8-jre-alpine AS clientui
# Add folder :
RUN mkdir /tmp/app
# copy JAR into image
COPY ./clientui/target/clientui-0.0.1-SNAPSHOT.jar /tmp/app
#api port
EXPOSE 8080
# run java app:
CMD java -jar /tmp/app/clientui-0.0.1-SNAPSHOT.jar