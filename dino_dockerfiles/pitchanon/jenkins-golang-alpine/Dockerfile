FROM alpine:3.4

# Packages
RUN echo http://dl-4.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories && \
    apk update && \
    apk upgrade && \
    apk add openjdk7-jre-base java-common && \
    rm -rf /var/cache/apk/*

RUN apk add --no-cache \
    ca-certificates \
    curl \
    bash \
    git \
    zip \
    wget \
    # docker \
    openssh \
    ttf-dejavu && \
    rm -rf /var/cache/apk/*

# Install Jenkins
ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk/jre
ENV JENKINS_HOME /var/jenkins_home
ENV JENKINS_SLAVE_AGENT_PORT 50000
ENV JENKINS_VERSION 2.7.3

# Docker compose
# RUN echo "Installing docker-compose" && \
#     curl -sSL --create-dirs --retry 1 https://github.com/docker/compose/releases/download/1.6.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && \
#     chmod +x /usr/local/bin/docker-compose

# Jenkins
RUN echo "Installing jenkins ${JENKINS_VERSION}" && \
    curl -sSL --create-dirs --retry 1 http://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war -o /usr/share/jenkins/jenkins.war

# Install Go
ENV GOLANG_VERSION 1.7
ENV GOLANG_SRC_URL https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz
ENV GOLANG_SRC_SHA256 72680c16ba0891fcf2ccf46d0f809e4ecf47bbf889f5d884ccb54c5e9a17e1c0

RUN set -ex \
	&& apk add --no-cache --virtual .build-deps \
		bash \
		gcc \
		musl-dev \
		openssl \
		go \
	\
	&& export GOROOT_BOOTSTRAP="$(go env GOROOT)" \
	\
	&& wget -q "$GOLANG_SRC_URL" -O golang.tar.gz \
	&& echo "$GOLANG_SRC_SHA256  golang.tar.gz" | sha256sum -c - \
	&& tar -C /usr/local -xzf golang.tar.gz \
	&& rm golang.tar.gz \
	&& cd /usr/local/go/src \
	&& ./make.bash \
	\
	&& rm -rf /*.patch \
	&& apk del .build-deps

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
WORKDIR $GOPATH

EXPOSE 8080
EXPOSE 8443
EXPOSE 50000

CMD exec java -jar /usr/share/jenkins/jenkins.war