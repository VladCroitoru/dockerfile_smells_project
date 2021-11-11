FROM openjdk:11

ARG JMETER_VERSION=5.4.1

COPY . /usr/src/myapp
WORKDIR /usr/src/myapp

RUN apt-get clean && \
apt-get update && \
apt-get -qy install \
wget \
telnet \
iputils-ping \
unzip

RUN   mkdir /jmeter \
&& cd /jmeter/ \
&& wget https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-$JMETER_VERSION.tgz \
&& tar -xzf apache-jmeter-$JMETER_VERSION.tgz \
&& rm apache-jmeter-$JMETER_VERSION.tgz

RUN cd /jmeter/apache-jmeter-$JMETER_VERSION/ && wget -q -O /tmp/JMeterPlugins-Standard-1.4.0.zip https://jmeter-plugins.org/downloads/file/JMeterPlugins-Standard-1.4.0.zip && unzip -n /tmp/JMeterPlugins-Standard-1.4.0.zip && rm /tmp/JMeterPlugins-Standard-1.4.0.zip

ENV JMETER_HOME /jmeter/apache-jmeter-$JMETER_VERSION/
		
ENV PATH $JMETER_HOME/bin:$PATH

EXPOSE 60000

COPY entrypoint.sh /usr/local/bin/

ENTRYPOINT ["entrypoint.sh"]