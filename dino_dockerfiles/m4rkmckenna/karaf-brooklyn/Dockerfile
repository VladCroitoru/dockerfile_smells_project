FROM java:8-jre-alpine
MAINTAINER Mark McKenna <m4rkmckenna@gmail.com>
LABEL version="0.10.0-SNAPSHOT"
ENV brooklyn_version 0.10.0-SNAPSHOT
ENV repository snapshots
RUN apk upgrade --update ; \
    apk add bash openssl curl ; \
    rm -rf /var/lib/apt/lists/* ; \
    rm -rf /var/cache/apk/* ;
RUN curl -s -L "https://repository.apache.org/service/local/artifact/maven/redirect?r=${repository}&g=org.apache.brooklyn&a=apache-brooklyn&v=${brooklyn_version}&p=tar.gz" -o apache-brooklyn.tar.gz ; \
    tar zxf apache-brooklyn.tar.gz ; \
    rm -f apache-brooklyn.tar.gz ; \
    mv /apache-brooklyn-${brooklyn_version} /apache-brooklyn ;
WORKDIR /apache-brooklyn
VOLUME [ "/root/.brooklyn", "/root/.ssh" ]
EXPOSE 8081 8101
ENTRYPOINT [ "./bin/karaf"]
