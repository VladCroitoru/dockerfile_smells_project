# Package the application as a war file
FROM maven:3.8.3-ibmjava-8-alpine AS builder
LABEL maintainer="IBM Java Engineering at IBM Cloud"
COPY pom.xml ./
COPY src src/
RUN mvn clean package

# Copy the war file over to the open liberty image
FROM openliberty/open-liberty:kernel-java8-openj9-ubi

COPY --from=builder --chown=1001:0 src/main/liberty/config/ /config/
COPY --from=builder --chown=1001:0 target/*.war /config/apps/

ENV PORT 9080

EXPOSE 9080

RUN configure.sh
