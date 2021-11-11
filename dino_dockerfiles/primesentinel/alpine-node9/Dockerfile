FROM node:9.4.0-alpine
RUN apk update

# Install essentials
RUN apk add --no-cache make git zip curl wget
RUN apk add ca-certificates
RUN apk add --update nodejs

# Install cloudfoundry-cli
RUN curl -L "https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" | tar -zx
RUN mv cf /usr/local/bin

# add a simple script that can auto-detect the appropriate JAVA_HOME value
# based on whether the JDK or only the JRE is installed
RUN { \
		echo '#!/bin/sh'; \
		echo 'set -e'; \
		echo; \
		echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
	} > /usr/local/bin/docker-java-home \
	&& chmod +x /usr/local/bin/docker-java-home
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/jre
ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin

ENV JAVA_VERSION 8u131
ENV JAVA_ALPINE_VERSION 8.131.11-r2

RUN set -x \
	&& apk add --no-cache \
		openjdk8-jre="$JAVA_ALPINE_VERSION" \
	&& [ "$JAVA_HOME" = "$(docker-java-home)" ]		

RUN apk --no-cache add --virtual native-deps \
  g++ gcc libgcc libstdc++ linux-headers make python && \
  rm -rf node_modules &&\
  npm install --quiet node-gyp -g &&\
  npm install bower -g &&\
  npm install node-gyp -g
  #npm install phantomjs -g &&\
  #npm install phantomjs-prebuilt@2.1.14 --ignore-scripts &&\
  #npm install -g karma-cli &&\
  #npm rebuild
  #npm --add-python-to-path='true' --debug install --global windows-build-tools
  #npm install --bower
  #apk del native-deps
