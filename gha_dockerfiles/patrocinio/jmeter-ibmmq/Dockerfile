# inspired by https://github.com/hauptmedia/docker-jmeter  and
# https://github.com/hhcordero/docker-jmeter-server/blob/master/Dockerfile
FROM alpine:3.12

MAINTAINER Just van den Broecke<just@justobjects.nl>

ARG JMETER_VERSION="5.3"
ENV JMETER_HOME /opt/apache-jmeter-${JMETER_VERSION}
ENV	JMETER_BIN	${JMETER_HOME}/bin
ENV	JMETER_DOWNLOAD_URL  https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-${JMETER_VERSION}.tgz

# Install extra packages
# Set TimeZone, See: https://github.com/gliderlabs/docker-alpine/issues/136#issuecomment-612751142
ARG TZ="Europe/Amsterdam"
ENV TZ ${TZ}
RUN    apk update \
	&& apk upgrade \
	&& apk add ca-certificates \
	&& update-ca-certificates \
	&& apk add --update openjdk8-jre tzdata curl unzip bash \
	&& apk add --no-cache nss \
	&& rm -rf /var/cache/apk/* \
	&& mkdir -p /tmp/dependencies  \
	&& curl -L --silent ${JMETER_DOWNLOAD_URL} >  /tmp/dependencies/apache-jmeter-${JMETER_VERSION}.tgz  \
	&& mkdir -p /opt  \
	&& tar -xzf /tmp/dependencies/apache-jmeter-${JMETER_VERSION}.tgz -C /opt  \
	&& rm -rf /tmp/dependencies
	
# Remove geronimo library
RUN rm /opt/apache-jmeter-${JMETER_VERSION}/lib/geronimo-jms_1.1_spec-1.1.1.jar

# TODO: plugins (later)
# && unzip -oq "/tmp/dependencies/JMeterPlugins-*.zip" -d $JMETER_HOME
RUN mkdir ${JMETER_HOME}/lib/ibmmq
COPY lib/ibmmq ${JMETER_HOME}/lib/ibmmq
RUN echo "user.classpath=lib/ibmmq" >> ${JMETER_HOME}/bin/user.properties
RUN echo "jmeter.reportgenerator.temp_dir=/tmp" >> ${JMETER_HOME}/bin/user.properties

# Copy Test file
#RUN mkdir -p ${JMETER_HOME}/tests/ibmmq
#RUN chmod -R 777 ${JMETER_HOME}/tests/ibmmq
#COPY tests/ibmmq/MQ.jmx tests/ibmmq/clientkey.jks ${JMETER_HOME}/tests/ibmmq
COPY test_kube.sh ${JMETER_HOME}

# Set global PATH such that "jmeter" command is found
ENV PATH $PATH:$JMETER_BIN

# Entrypoint has same signature as "jmeter" command
COPY entrypoint.sh /

WORKDIR	${JMETER_HOME}

#ENTRYPOINT ["/entrypoint.sh"]
#ENTRYPOINT sleep 3600
ENTRYPOINT ./test_kube.sh