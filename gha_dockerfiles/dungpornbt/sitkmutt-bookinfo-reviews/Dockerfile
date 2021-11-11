# MULTISTAGE Build
FROM gradle:6.0.1-jdk11 AS builder
WORKDIR /opt/java/
COPY . /opt/java/
RUN gradle clean build

# MULTISTAGE Run
FROM websphere-liberty:19.0.0.12-kernel-java8-ibmjava

# Copy .jar file from build stage
COPY --from=builder /opt/java/build/libs/java.war /opt/ibm/wlp/usr/servers/defaultServer/apps/reviews.war
# Copy server configuration
COPY config/server.xml /opt/ibm/wlp/usr/servers/defaultServer/

RUN /opt/ibm/wlp/bin/installUtility install  --acceptLicense /opt/ibm/wlp/usr/servers/defaultServer/server.xml

EXPOSE 9080

CMD ["/opt/ibm/wlp/bin/server", "run", "defaultServer"]
