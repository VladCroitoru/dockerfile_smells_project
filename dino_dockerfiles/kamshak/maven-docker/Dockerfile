FROM java:8-alpine

############################# DOCKER #############################
 
RUN apk add --no-cache \
		ca-certificates \
		curl \
		openssl

ENV DOCKER_BUCKET test.docker.com
ENV DOCKER_VERSION 17.05.0-ce-rc1
ENV DOCKER_SHA256 4561742c2174c01ffd0679621b66d29f8a504240d79aa714f6c58348979d02c6

RUN set -x \
	&& curl -fSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o docker.tgz \
	&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \
	&& tar -xzvf docker.tgz \
	&& mv docker/* /usr/local/bin/ \
	&& rmdir docker \
	&& rm docker.tgz \
	&& docker -v
	
############################# DOCKER-COMPOSE ####################
ENV GLIBC 2.23-r3

RUN apk update && apk add --no-cache openssl ca-certificates && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$GLIBC/glibc-$GLIBC.apk && \
    apk add --no-cache glibc-$GLIBC.apk && rm glibc-$GLIBC.apk && \
    ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ && \
    ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib

ADD https://github.com/docker/compose/releases/download/1.13.0/docker-compose-Linux-x86_64 /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

############################# MAVEN #############################

RUN apk add --update ca-certificates && rm -rf /var/cache/apk/* && \
  find /usr/share/ca-certificates/mozilla/ -name "*.crt" -exec keytool -import -trustcacerts \
  -keystore /usr/lib/jvm/java-1.8-openjdk/jre/lib/security/cacerts -storepass changeit -noprompt \
  -file {} -alias {} \; && \
  keytool -list -keystore /usr/lib/jvm/java-1.8-openjdk/jre/lib/security/cacerts --storepass changeit

ENV MAVEN_VERSION 3.3.9
ENV MAVEN_HOME /usr/lib/mvn
ENV PATH $MAVEN_HOME/bin:$PATH

RUN wget http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  tar -zxvf apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  rm apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  mv apache-maven-$MAVEN_VERSION /usr/lib/mvn

RUN mkdir -p /usr/src/app

############################# GCLOUD #############################

RUN apk update && apk add wget bash python git && rm -rf /var/cache/apk/*

RUN wget https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz --no-check-certificate \
    && tar zxvf google-cloud-sdk.tar.gz \
    && rm google-cloud-sdk.tar.gz \
    && ls -l \
    && ./google-cloud-sdk/install.sh --usage-reporting=true --path-update=true

# Add gcloud to the path
ENV PATH /google-cloud-sdk/bin:$PATH

# Configure gcloud for your project
RUN yes | gcloud components update
RUN yes | gcloud components update preview
RUN yes | gcloud components install beta

############################# WARM MAVEN CACHE #############################

WORKDIR /usr/src/app

COPY pom.xml /usr/src/app/pom.xml
RUN mvn dependency:resolve-plugins
RUN mvn dependency:go-offline
RUN mvn clean install; mvn resources:resources; mvn compiler:compile; mvn surefire:test; mvn jar:jar; mvn spring-boot:repackage; mvn scm:tag; mvn docker:build; rm -rf ./*; exit 0
