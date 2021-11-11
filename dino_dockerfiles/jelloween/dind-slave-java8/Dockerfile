# Based on vixns/java8 and tehranian/dind-jenkins-slave

FROM tehranian/dind-jenkins-slave

# Install JDK 8 (latest edition)
RUN \ 
	export DEBIAN_FRONTEND=noninteractive && \ 
	apt-get update && \ 
	apt-get upgrade -y && \
	echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list && \ 
	echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list && \ 
	apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && \
    	apt-get update && \
    	echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    	apt-get -y install oracle-java8-installer && \
    	update-alternatives --display java && \
    	apt-get -y install oracle-java8-set-default && \
    	rm -fr /var/cache/oracle-jdk8-installer && \ 
	apt-get clean && \ 
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
