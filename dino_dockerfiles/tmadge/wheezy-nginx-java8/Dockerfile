
FROM    		nginx:1.7.10
MAINTAINER 	Trevor Madge <tmadge@gmail.com>

RUN 	echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" > /etc/apt/sources.list.d/webupd8team-java.list && \
			echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections && \
			apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \
			#apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && \
			apt-get update && \
			apt-get install -y oracle-java8-installer && \
			apt-get clean && \
			rm -rf /var/cache/oracle-jdk8-installer

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
