FROM java:8-alpine

ENV GROOVY_VERSION 2.4.7

RUN apk update && \
    apk add ca-certificates wget bash && \
    update-ca-certificates

WORKDIR /root/groovy
RUN wget https://bintray.com/artifact/download/groovy/maven/apache-groovy-binary-${GROOVY_VERSION}.zip && \
    unzip apache-groovy-binary-${GROOVY_VERSION}.zip
ENV GROOVY_HOME /root/groovy/groovy-${GROOVY_VERSION}
WORKDIR /root/groovy/groovy-${GROOVY_VERSION}
CMD bash bin/groovysh

