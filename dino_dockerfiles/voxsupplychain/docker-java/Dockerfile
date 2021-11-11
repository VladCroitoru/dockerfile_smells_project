FROM gliderlabs/alpine
MAINTAINER Todor Todorov <todor@peychev.com>

ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk

RUN  apk add --update openjdk7-jre-base bash \
	&& rm -rf /var/cache/apk/*

RUN echo "networkaddress.cache.ttl=10" >> $JAVA_HOME/jre/lib/security/java.security

