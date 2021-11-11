FROM java:openjdk-8-jre-alpine

# Alpine + OpenJDK 8.x + Wildfly 12 servlet (Undertow) docker image

MAINTAINER degenerate76

ENV WILDFLY_BASE_URL http://download.jboss.org/wildfly
ENV WILDFLY_VERSION 12.0.0.Final

RUN apk --update --no-cache --virtual=build-dependencies add curl ca-certificates tar && \
	curl ${WILDFLY_BASE_URL}/${WILDFLY_VERSION}/servlet/wildfly-servlet-${WILDFLY_VERSION}.tar.gz > wildfly-servlet.tar.gz && \
	tar -xzf wildfly-servlet.tar.gz && \
	mv wildfly-servlet-${WILDFLY_VERSION} /wildfly-servlet && \
	rm -f wildfly-servlet.tar.gz && \
	rm -rf /wildfly-servlet/welcome-content /wildfly-servlet/docs && \
	apk del build-dependencies

ENV LAUNCH_JBOSS_IN_BACKGROUND true

EXPOSE 8080

CMD [ "/wildfly-servlet/bin/standalone.sh", "-b", "0.0.0.0" ]
