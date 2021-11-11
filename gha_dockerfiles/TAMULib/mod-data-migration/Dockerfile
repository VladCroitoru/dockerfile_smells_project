# build base image
FROM maven:3-openjdk-11-slim as maven

# copy pom.xml
COPY ./pom.xml ./pom.xml

# copy src files
COPY ./src ./src

# Copy the sub-modules to the container
COPY ./mod-data-import-converter-storage ./mod-data-import-converter-storage
COPY ./mod-inventory-storage ./mod-inventory-storage
COPY ./mod-organizations-storage ./mod-organizations-storage
COPY ./mod-users ./mod-users
COPY ./mod-circulation ./mod-circulation
COPY ./mod-feesfines ./mod-feesfines
COPY ./mod-notes ./mod-notes
COPY ./mod-user-import ./mod-user-import
COPY ./mod-orders ./mod-orders

# build
RUN mvn package

# final base image
FROM openjdk:11-jre-slim

# set deployment directory
WORKDIR /mod-data-migration

# copy over the built artifact from the maven image
COPY --from=maven /target/mod-data-migration*.jar ./mod-data-migration.jar

# environment
ENV SERVER_PORT='9000'
ENV ACTIVE_PROCESSOR_COUNT='12'
ENV TIME_ZONE='America/Chicago'

# expose port
EXPOSE ${SERVER_PORT}

# run java command
CMD java -XX:ActiveProcessorCount=${ACTIVE_PROCESSOR_COUNT} -Duser.timezone=${TIME_ZONE} -jar ./mod-data-migration.jar
