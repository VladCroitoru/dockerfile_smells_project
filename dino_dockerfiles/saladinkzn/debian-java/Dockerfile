from debian:jessie

run echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections \
	&& echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list \ 
	&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list \
	&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 \
	&& apt-get update \
	&& apt-get install -y oracle-java8-installer \
	&& rm -r /var/cache/oracle-jdk8-installer \
	&& rm -r /usr/lib/jvm/java-8-oracle/lib/missioncontrol \
	&& rm -r /usr/lib/jvm/java-8-oracle/lib/visualvm \
	&& rm /usr/lib/jvm/java-8-oracle/src.zip \
	&& rm /usr/lib/jvm/java-8-oracle/javafx-src.zip \
	&& apt-get clean

env JAVA_HOME /usr/lib/jvm/java-8-oracle

cmd ["java"]
