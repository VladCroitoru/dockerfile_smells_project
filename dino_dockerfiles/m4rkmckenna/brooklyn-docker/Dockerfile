FROM java:8-jre-alpine
MAINTAINER Mark McKenna <m4rkmckenna@gmail.com>
VOLUME [ "/root/.brooklyn", "/root/.ssh", "/apache-brooklyn/deploy", "/apache-brooklyn/log" ]
EXPOSE 8081 8101 8443
ENTRYPOINT [ "/apache-brooklyn/bin/karaf", "server" ]
LABEL version="0.11.0-SNAPSHOT"
ENV brooklyn_version=0.11.0-SNAPSHOT repository=snapshots
RUN apk upgrade --update ; \
    apk add bash openssl curl ; \
	rm -rf /var/lib/apt/lists/* ; \
	rm -rf /var/cache/apk/* ; \
    curl -L "https://repository.apache.org/service/local/artifact/maven/redirect?r=${repository}&g=org.apache.brooklyn&a=apache-brooklyn&v=${brooklyn_version}&p=tar.gz" -o apache-brooklyn.tar.gz ; \
    tar zxf apache-brooklyn.tar.gz ; \
    rm -f apache-brooklyn.tar.gz ; \
	mv /apache-brooklyn-${brooklyn_version} /apache-brooklyn
COPY ["config/etc","/apache-brooklyn/etc/"]
