FROM java:8
MAINTAINER Paulo Sigrist <paulo.sigrist@gmail.com>

# Create the base folders
RUN mkdir -p /data
RUN mkdir -p /opt/wiremock

# Download the wiremock standalone into /opt/wiremock folder
ADD https://repo1.maven.org/maven2/com/github/tomakehurst/wiremock-standalone/2.18.0/wiremock-standalone-2.18.0.jar /opt/wiremock/

# Set /data as workdir
WORKDIR /data

# Start the wiremock
ENTRYPOINT ["java", "-jar", "/opt/wiremock/wiremock-standalone-2.18.0.jar"]
