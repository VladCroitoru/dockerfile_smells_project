############################################################
# Dockerfile to build WebApollo container image for the eBioKit
# Based on tomcat:8.5-jre8-alpine
# Version 0.2 August 2017
############################################################

# Set the base image to tomcat:8-jre8
FROM tomcat:8.5-jre8-alpine

# File Maintainer
MAINTAINER Rafael Hernandez <ebiokit@gmail.com>

################## BEGIN INSTALLATION ######################

#ADD FILES AND SET PERMISSIONS
ENV WEBAPOLLO_VERSION=7b304aac81f7dab77165f37bf210a6b3cb1b8080 PERL5LIB=$PERL5LIB:/extlib/lib/perl5/
COPY config/build.sh /bin/

#INSTALL THE DEPENDENCIES
RUN apk update && \
	apk add --update tar && \
	apk add curl ca-certificates bash nodejs git postgresql postgresql-client \
		maven libpng make g++ zlib-dev expat-dev nodejs-npm sudo

RUN npm install -g bower

RUN apk add openjdk8 openjdk8-jre && \
	cp /usr/lib/jvm/java-1.8-openjdk/lib/tools.jar /usr/lib/jvm/java-1.8-openjdk/jre/lib/ext/tools.jar

RUN adduser -s /bin/bash -D -h /apollo apollo && \
	curl -L https://github.com/GMOD/Apollo/archive/${WEBAPOLLO_VERSION}.tar.gz | \
	tar xzf - --strip-components=1 -C /apollo

ADD config/apollo-config.groovy /apollo/apollo-config.groovy

RUN apk add perl perl-dev db db-dev wget

RUN chown -R apollo:apollo /apollo && \
	chmod +x /bin/build.sh && \
	sudo -u apollo /bin/build.sh && \
	ln -s /usr/local/tomcat/webapps/ROOT/jbrowse /jbrowse

RUN curl -L -o /chado.sql.gz https://github.com/erasche/chado-schema-builder/releases/download/1.31-jenkins97/chado-1.31.sql.gz

RUN apk del curl nodejs git libpng make g++ nodejs-npm openjdk8 sudo

COPY config/launch.sh /bin/

##################### INSTALLATION END #####################
ENV CONTEXT_PATH ROOT
VOLUME ["/data"]
CMD "/bin/launch.sh"
