# https://hub.docker.com/r/jenkins/jenkins/
# doc at https://github.com/jenkinsci/docker/blob/master/README.md

FROM jenkins/jenkins:alpine

# jenkins_home:/var/jenkins_home

#-----------------------
# Installing more tools
#-------------------------

USER root
#RUN apt-get update && apt-get install -y ruby make more-thing-here
# drop back to the regular jenkins user - good practice

# Environments
ENV TIMEZONE            Europe/Paris
ENV PHP_MEMORY_LIMIT    -1
ENV JENKINS_HOME /var/jenkins_home

RUN set -ex \
	&& apk add --no-cache wget \
	&& apk add --update tzdata \
	&& cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \
	&& echo "${TIMEZONE}" > /etc/timezone \
	&& apk add --no-cache php7-common php7-pear \
	&& apk add --no-cache php7-iconv php7-json php7-phar php7-gd  \
	&& apk add --no-cache php7-dev  \
	&& apk add --no-cache php7-mysqli \
	&& apk add --no-cache php7-sqlite3 \
	&& apk add --no-cache php7-pdo_mysql \
	&& apk add --no-cache php7-pdo_sqlite \
	&& apk add --no-cache php7-curl \
	&& apk add --no-cache php7-xdebug \
	&& apk add --no-cache php7-xsl \
	&& apk add --no-cache php7-dom \
	&& apk add --no-cache php7-mbstring \
	&& apk add --no-cache php7-mcrypt \
	&& apk add --no-cache php7-bz2 php7-zip php7-zlib\
	&& apk add --no-cache php7-ctype \
	&& apk add --no-cache php7-simplexml \
	&& apk add --no-cache php7-tokenizer \
	&& apk add --no-cache php7-xmlwriter \
	&& apk add --no-cache php7-gmp \
	&& apk add --no-cache --virtual .fetch-deps openssl \
	&& apk add --no-cache php7-openssl \
	&& sed -i "s|;*date.timezone =.*|date.timezone = ${TIMEZONE}|i" /etc/php7/php.ini \
	&& sed -i "s|;*memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|i" /etc/php7/php.ini \
	&& apk del tzdata \
	&& rm -rf /var/cache/apk/*

RUN set -xe; \
	mkdir -p /usr/local/bin; \
	wget -qO- https://getcomposer.org/installer | php7 -- --install-dir=/usr/local/bin --filename=composer; \
	chown jenkins:jenkins /usr/local/bin/composer; \
	rm -rf \
        /root/.composer \
		;
	
COPY cli.sh /usr/local/bin/cli.sh
RUN set -xe \
    && chown -R jenkins:jenkins /usr/share/jenkins \
    && chown jenkins:jenkins /usr/local/bin/cli.sh \
    && chmod u+x  /usr/local/bin/cli.sh

USER jenkins
env PATH="/usr/local/bin:${PATH}"
#USER root
#CMD su jenkins -c export | egrep " PATH="
#USER jenkins

#-------
#
#-------

#executors.groovy
#
#import jenkins.model.*
#Jenkins.instance.setNumExecutors(5)

#COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy
#-----------------
# Passing Jenkins launcher parameters
#-----------------
#COPY https.pem /var/lib/jenkins/cert
#COPY https.key /var/lib/jenkins/pk
#ENV JENKINS_OPTS --httpPort=-1 --httpsPort=8083 --httpsCertificate=/var/lib/jenkins/cert --httpsPrivateKey=/var/lib/jenkins/pk
#EXPOSE 8083
#ENV JENKINS_SLAVE_AGENT_PORT 50001


#-----
# Preinstalling plugins
#------

#RUN /usr/local/bin/install-plugins.sh docker-slaves github-branch-source:1.8

COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN set -xe \
    && /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt


