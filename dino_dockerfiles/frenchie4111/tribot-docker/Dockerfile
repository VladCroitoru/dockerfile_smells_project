FROM ubuntu:14.04

# Install base ubuntu packages 
RUN \
	sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
	apt-get update && \
	apt-get -y upgrade && \
	apt-get install -y build-essential && \
	apt-get install -y software-properties-common && \
	apt-get install -y byobu curl git htop man unzip vim wget && \
	rm -rf /var/lib/apt/lists/*

# Install LXDE and VNC server.
RUN \
	apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get install -y lxde-core lxterminal firefox tightvncserver && \
	rm -rf /var/lib/apt/lists/*

# Install Java
RUN \
	echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
	add-apt-repository -y ppa:webupd8team/java && \
	apt-get update && \
	apt-get install -y oracle-java8-installer && \
	rm -rf /var/lib/apt/lists/* && \
	rm -rf /var/cache/oracle-jdk8-installer

# Install TRiBot dependencies
RUN \
	apt-get update && \
	apt-get install -y libxslt1.1

# Set user
ENV USER root

# Set WORKDIR
WORKDIR "/root"

COPY "startup.sh" "/root/"

# Download tribot
RUN wget https://tribot.org/bin/TRiBot_Loader.jar

ENTRYPOINT "/root/startup.sh"

# Expose ports.
EXPOSE 5901
