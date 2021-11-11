FROM ubuntu:14.04
MAINTAINER Predrag Knezevic <pedjak@gmail.com>

RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV JDK7_URL https://repo.datastax.com/jdk-distributions/jdk-7u80-linux-x64.tar.gz
ENV JDK8_URL https://repo.datastax.com/jdk-distributions/jdk-8u181-linux-x64.tar.gz
ENV JDK11_URL https://repo.datastax.com/jdk-distributions/jdk-11.0.1_linux-x64_bin.tar.gz

COPY locale /etc/default/locale

RUN apt-get -qq update && \
	apt-get install -y apt-transport-https ca-certificates && \
	apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D && \
	echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" >> /etc/apt/sources.list && \
	apt-get -qq update && \
	apt-get install -y openssh-server nfs-common portmap parallel docker-engine=1.11.2-0~trusty build-essential python-software-properties software-properties-common wget curl git fontconfig  unzip && \
# SSH server
	sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd && \
	sed -i 's|PermitRootLogin without-password|PermitRootLogin yes|g' /etc/ssh/sshd_config && \
	mkdir -p /var/run/sshd && \
	mkdir -p /opt/jdk && \
	mkdir -p /tmp/download && \
	rm -rf /var/lib/apt/lists/* 

# Java 1.7
RUN cd /tmp/download && wget $JDK7_URL && \
	tar -zxf `ls -1 *.tar.gz` -C /opt/jdk && \
	rm * -rf 

# Java 1.8
RUN cd /tmp/download &&	 wget $JDK8_URL && \
	tar -zxf `ls -1 *.tar.gz` -C /opt/jdk && \
	rm * -rf

# Java 11
RUN cd /tmp/download &&	 wget $JDK11_URL && \
	tar -zxf `ls -1 *.tar.gz` -C /opt/jdk && \
	rm * -rf

# Set the default java version to 1.8
RUN	update-alternatives --install /usr/bin/java java `find /opt/jdk -name jdk1.8*`/bin/java 100 && \
	update-alternatives --install /usr/bin/javac javac `find /opt/jdk -name jdk1.8*`/bin/javac 100

# Set Java and Maven env variables
#RUN echo "JDK7_HOME=\"`find /opt/jdk -name jdk1.7*`\"" >> /etc/environment
#RUN echo "JAVA_HOME=\"`find /opt/jdk -name jdk1.7*`\"" >> /etc/environment
#RUN echo "JDK8_HOME=\"`find /opt/jdk -name jdk1.8*`\"" >> /etc/environment
#RUN echo "JDK11_HOME=\"`find /opt/jdk -name jdk11*`\"" >> /etc/environment

# Maven 3.0.5
RUN cd /tmp/download &&	wget http://ftp.fau.de/apache/maven/maven-3/3.0.5/binaries/apache-maven-3.0.5-bin.tar.gz && \
	mkdir -p /opt/maven && \
	tar -zxf apache-maven-3.0.5-bin.tar.gz -C /opt/maven && \
	ln -s /opt/maven/apache-maven-3.0.5/bin/mvn /usr/bin && \
	rm * -rf

#Groovy 2.4
RUN cd /tmp/download && wget http://dl.bintray.com/groovy/maven/groovy-binary-2.4.3.zip && \
	unzip -d /opt groovy-binary-2.4.3.zip && \
	ln -s /opt/groovy-2.4.3/bin/groovy /usr/bin && \
	rm * -rf


ENV M2_HOME /opt/maven/apache-maven-3.0.5
#ENV JAVA_OPTS -Xmx2G -Xms2G -XX:PermSize=256M -XX:MaxPermSize=256m

# Load scripts
COPY bootstrap bootstrap
RUN chmod +x -Rv bootstrap

USER root

# Add user jenkins to the image
RUN adduser --quiet jenkins && \
	adduser jenkins sudo && \
	echo "jenkins:jenkins" | chpasswd

# Adjust perms for jenkins user
#RUN chown -R jenkins /opt/nvm
RUN echo "JDK7_HOME=\"`find /opt/jdk -name jdk1.7*`\"" >> /etc/environment && \
	echo "JDK8_HOME=\"`find /opt/jdk -name jdk1.8*`\"" >> /etc/environment && \
	echo "JDK11_HOME=\"`find /opt/jdk -name jdk-11*`\"" >> /etc/environment && \
	chown jenkins /home/jenkins/.profile

# Standard SSH port
EXPOSE 22

# Startup services when running the container
ENTRYPOINT ["./bootstrap/init.sh"]
