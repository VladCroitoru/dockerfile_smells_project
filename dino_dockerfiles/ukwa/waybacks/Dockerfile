FROM maven:3 AS build-env
# originally based on UNB Libraries Dockerfile
MAINTAINER Andrew Jackson "anj@anjackson.net"

# Now build our overlays:
COPY pom.xml /waybacks/pom.xml
COPY wayback-ukwa /waybacks/wayback-ukwa
COPY wayback-ldwa /waybacks/wayback-ldwa
COPY wayback-qa /waybacks/wayback-qa

RUN cd waybacks && \
  mvn install -DskipTests

# Now set up tomcat:
FROM tomcat:7

# Cleanup webapps directory
RUN cd webapps && rm -rf *

# Tweak Tomcat configuration
COPY docker/server.xml conf/server.xml
COPY docker/logging.properties conf/logging.properties

# Install ICU4J in the system JVM for broader language support
RUN \
  curl -O http://download.icu-project.org/files/icu4j/58.2/icu4j-58_2.jar && \
  curl -O http://download.icu-project.org/files/icu4j/58.2/icu4j-localespi-58_2.jar && \ 
  mv icu4j-* /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/ext/

# Copy in built WARs:
COPY --from=build-env /waybacks/wayback-qa/target/*.war /waybacks/wayback-qa/target/
COPY --from=build-env /waybacks/wayback-ukwa/target/*.war /waybacks/wayback-ukwa/target/
COPY --from=build-env /waybacks/wayback-ldwa/target/*.war /waybacks/wayback-ldwa/target/

# Define runtime properties
EXPOSE 8080 8090
ENV JAVA_OPTS -Xmx1g

# Use oukwa|ldukwa|qa for Open UKWA, LD UKWA or QA UKWA versions
ENV UKWA_OWB_VERSION=qa 

VOLUME /data

#Fire up tomcat, copying desired WAR into place first
COPY docker/start.sh /

CMD /start.sh
