FROM khirin/alpine

ARG	UID="2000"
ARG	GID="2000"
ARG	PORT="8080"

LABEL 	maintainer="khirin" \
	name="Tomcat Image" \
        tomcat_version="8.0.41" \
	date="20170315" \
        image_version="1.7" \
	user="tomcat" \
	uid=${UID} \
	group="tomcat" \
	gid=${GID}

COPY ["sources/alpine_docker-java-home", "sources/init.sh", "sources/apache-tomcat-8.0.41.tar.gz", "/tmp/"]

RUN	addgroup -g ${GID} tomcat \
	&& adduser -D -G tomcat -g "Tomcat User" -s /bin/sh -u ${UID} tomcat \
	&& apk --update add openjdk8-jre \
	&& rm -rf /var/cache/apk/* \
	&& mkdir -p /var/lib/tomcat \
	&& tar -xf /tmp/apache-tomcat-8.0.41.tar.gz -C /var/lib/tomcat/ --strip-components=1 \
	&& rm /tmp/apache-tomcat-8.0.41.tar.gz \
	&& /tmp/init.sh

ENV	CATALINA_HOME="/var/lib/tomcat" \
	TOMCAT_HOME="/var/lib/tomcat" \
	JAVA_HOME=$(docker-java-home)

EXPOSE ${PORT}

USER tomcat

ENTRYPOINT ["/bin/sh", "-c", "${CATALINA_HOME}/bin/catalina.sh run"]
