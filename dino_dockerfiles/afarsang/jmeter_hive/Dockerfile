FROM openjdk:8-jre
ENV JMETER_VERSION=3.2
RUN wget http://www.eu.apache.org/dist/jmeter/binaries/apache-jmeter-${JMETER_VERSION}.tgz && \
	tar -xzf apache-jmeter-${JMETER_VERSION}.tgz -C /usr/local/
ENV JMETER_HOME=/usr/local/apache-jmeter-${JMETER_VERSION}
ENV PATH=${JMETER_HOME}/bin:${PATH}

COPY lib ${JMETER_HOME}/lib/ext/

RUN rm -rf apache-jmeter-${JMETER_VERSION}.tgz \
			${JMETER_HOME}/bin/examples \
			${JMETER_HOME}/bin/templates \
			${JMETER_HOME}/bin/*.cmd \
			${JMETER_HOME}/bin/*.bat \
			${JMETER_HOME}/docs \
			${JMETER_HOME}/printable_docs

EXPOSE 1099

ENTRYPOINT ["jmeter.sh","-n"]
