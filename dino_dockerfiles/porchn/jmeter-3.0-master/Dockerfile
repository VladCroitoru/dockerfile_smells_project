# Use porchn/jmeter-3.0-base

FROM porchn/jmeter-3.0-base
MAINTAINER Porchn
ENV JMETER_VERSION 3.0


# mkdir userconfig
#RUN mkdir -p /jmeter/userconfig
RUN mv /jmeter/apache-jmeter-${JMETER_VERSION}/bin/user.properties /jmeter/userconfig

# renew user.properties path
RUN perl -pi -e 's/user.properties=user.properties/user.properties=\/jmeter\/userconfig\/user.properties/g' /jmeter/apache-jmeter-${JMETER_VERSION}/bin/jmeter.properties


# Copy default config
COPY *.jmx /jmeter/jmxfile
COPY *.json /jmeter/mapping

# create volume
VOLUME ["/jmeter/jmxfile", "/jmeter/userconfig", "/jmeter/mapping"]

# Ports to be exposed from the container for JMeter Master
EXPOSE 60000
