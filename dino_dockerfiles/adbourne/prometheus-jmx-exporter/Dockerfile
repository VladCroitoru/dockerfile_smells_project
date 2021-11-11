FROM openjdk:8-jre-alpine
MAINTAINER Aaron Bourne <contact@aaronbourne.co.uk>

# The version of the jmx_prometheus_httpserver jar
ARG JAR_VERSION="0.1.0"

# The exporter user
ARG EXPORTER_USERNAME="exporter"

# Set the working directory
WORKDIR "/prometheus-jmx-exporter"

# Create an exporter user to run the application as
RUN addgroup -S ${EXPORTER_USERNAME} && adduser -S -g ${EXPORTER_USERNAME} ${EXPORTER_USERNAME}

# Add the jar from Maven Central
ADD "http://central.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_httpserver/${JAR_VERSION}/jmx_prometheus_httpserver-${JAR_VERSION}-jar-with-dependencies.jar" "jmx_prometheus_httpserver.jar"

# Copy over the configuration
COPY "resources/httpserver_config.yml" "httpserver_config.yml"

# Make the exporter user own the working directory
RUN chown -R exporter:exporter "/prometheus-jmx-exporter"

# Expose the metrics ports
EXPOSE "9999"

# Define the entrypoint and cmd
ENTRYPOINT ["java", "-jar", "jmx_prometheus_httpserver.jar"]
CMD [ "9999", "httpserver_config.yml" ]