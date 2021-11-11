# Use Ubuntu
FROM ubuntu
MAINTAINER Porchn

ENV JMETER_VERSION 3.0
ENV TZ=Asia/Bangkok

# Set the timezone.
RUN echo $TZ > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

# Install wger & JRE
RUN apt-get clean && \
	apt-get update && \
	apt-get -qy install \
				wget \
				default-jre-headless \
				telnet \
				iputils-ping \
				vim \
				unzip

# Install jmeter
RUN   mkdir /jmeter \
		&& cd /jmeter/ \
		&& mkdir jmxfile \
		&& mkdir userconfig \
		&& mkdir mapping \
		&& wget https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-${JMETER_VERSION}.tgz \
		&& tar -xzf apache-jmeter-${JMETER_VERSION}.tgz \
		&& rm apache-jmeter-${JMETER_VERSION}.tgz \
		&& mkdir /jmeter-plugins \
		&& cd /jmeter-plugins/ \
		&& wget https://jmeter-plugins.org/downloads/file/JMeterPlugins-ExtrasLibs-1.4.0.zip \
		&& unzip -o JMeterPlugins-ExtrasLibs-1.4.0.zip -d /jmeter/apache-jmeter-${JMETER_VERSION}/


# Set Jmeter Home
ENV JMETER_HOME /jmeter/apache-jmeter-${JMETER_VERSION}/

# Add Jmeter to the Path
ENV PATH $JMETER_HOME/bin:$PATH
