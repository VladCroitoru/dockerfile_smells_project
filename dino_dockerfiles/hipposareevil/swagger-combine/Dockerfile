FROM node:7.2-alpine

#############################
# install java and maven
# taken from:
# * https://hub.docker.com/_/java/  8-jdk-alpine
# -> https://github.com/docker-library/openjdk/blob/9a0822673dffd3e5ba66f18a8547aa60faed6d08/8-jdk/alpine/Dockerfile
# * https://hub.docker.com/_/maven/ 3.3-jdk8-alpine
# -> https://github.com/carlossg/docker-maven/blob/322d0dff5d0531ccaf47bf49338cb3e294fd66c8/jdk-8/Dockerfile

###########################
# java
ENV LANG C.UTF-8

# add a simple script that can auto-detect the appropriate JAVA_HOME value
# based on whether the JDK or only the JRE is installed
RUN { \
		echo '#!/bin/sh'; \
		echo 'set -e'; \
		echo; \
		echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
	} > /usr/local/bin/docker-java-home \
	&& chmod +x /usr/local/bin/docker-java-home
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin

ENV JAVA_VERSION 8u111
ENV JAVA_ALPINE_VERSION 8.111.14-r0

RUN set -x \
	&& apk add --no-cache \
		openjdk8="$JAVA_ALPINE_VERSION" \
	&& [ "$JAVA_HOME" = "$(docker-java-home)" ]



#######################
# maven
RUN apk add --no-cache curl tar bash

ARG MAVEN_VERSION=3.3.9
ARG USER_HOME_DIR="/root"

RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
  && curl -fsSL http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz \
    | tar -xzC /usr/share/maven --strip-components=1 \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"

####################
# install json->yaml
RUN npm install -g json2yaml


# Exposed 8080 to other containers
EXPOSE 8080

# packages for swagger-ui
RUN apk add --update nginx openssl curl bash

# setup for this version of nginx
RUN mkdir -p /run/nginx/
ENV NGINX_ROOT=/usr/share/nginx/html
RUN mkdir -p $NGINX_ROOT

# make directories used by the yaml merging
RUN mkdir -p /src /target


##########################
# grab the swagger-ui
# Inspired by https://hub.docker.com/r/schickling/swagger-ui/
#ENV SWAGGER_VERSION=2.2.8
ENV SWAGGER_VERSION=3.0.21
ENV SWAGGER_UI_FOLDER=swagger-ui-$SWAGGER_VERSION

# In the index.html file, Change the default swagger file to be 'swagger.yaml'
# The swagger.yaml file will be placed in the $NGINX_ROOT directory by the run.sh script.
RUN wget -qO- https://github.com/swagger-api/swagger-ui/archive/v$SWAGGER_VERSION.tar.gz | tar xvz; \
    cp -r $SWAGGER_UI_FOLDER/dist/* $NGINX_ROOT/;\
    sed -i.bak s#http://petstore.swagger.io/v2/swagger.json#swagger.yaml# $NGINX_ROOT/index.html; \
    cp $SWAGGER_UI_FOLDER/nginx.conf /etc/nginx/; \
    rm -rf $SWAGGER_UI_FOLDER;

#########################
# grab the merge-yaml java project
RUN wget https://github.com/cobbzilla/merge-yml/archive/master.zip; \
    unzip master.zip; \
    mvn -f merge-yml-master/pom.xml -P uberjar package; \
    rm -rf master.zip; \
    rm -rf ~/.m2


########################
# copy in our scripts
COPY waitforit.sh /
COPY run.sh /

ENTRYPOINT ["/run.sh"]
