FROM httpd:2.4
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get update

RUN echo 'deb http://httpredir.debian.org/debian jessie-backports main' > /etc/apt/sources.list.d/jessie-backports.list

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

# add a simple script that can auto-detect the appropriate JAVA_HOME value
# based on whether the JDK or only the JRE is installed
RUN { \
		echo '#!/bin/bash'; \
		echo 'set -e'; \
		echo; \
		echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
	} > /usr/local/bin/docker-java-home \
	&& chmod +x /usr/local/bin/docker-java-home
# set default java environment variable
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

ENV JAVA_VERSION 8u72
ENV JAVA_DEBIAN_VERSION 8u72-b15-1~bpo8+1

# see https://bugs.debian.org/775775
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872
ENV CA_CERTIFICATES_JAVA_VERSION 20140324

RUN set -x \
	&& apt-get update \
	&& apt-get install -y \
		openjdk-8-jdk="$JAVA_DEBIAN_VERSION" \
		ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \
	&& rm -rf /var/lib/apt/lists/* \
	&& [ "$JAVA_HOME" = "$(docker-java-home)" ]

# see CA_CERTIFICATES_JAVA_VERSION notes above
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure

RUN apt-get update \
    && apt-get install -y --no-install-recommends libaprutil1-ldap cron rsyslog \
    && apt-get -y install php5 php5-cli php5-mysqlnd php5-curl php5-ldap php5-mcrypt libapache2-mod-php5 vim && apt-get clean \
    && rm -r /var/lib/apt/lists/*
# Enable apache mods.
RUN a2enmod php5

# push your bootstrap script to root dir
#COPY ./env/bootstrap.sh /
#give execution rights to it 
#RUN chmod a+x /bootstrap.sh
VOLUME /euronews/app/html    
EXPOSE 80
CMD ["/bootstrap.sh"]