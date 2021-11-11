FROM ubuntu:16.04

MAINTAINER Debjeet Biswas <debjeet@leftshift.io>

# Variables
ENV DEBIAN_FRONTEND="noninteractive"
ENV JAVA_HOME="/usr/lib/jvm/java-7-oracle"
ENV JAVA8_HOME="/usr/lib/jvm/java-8-oracle"
ENV ANDROID_HOME="/usr/local/android-sdk-linux"
ENV GRADLE_HOME="/usr/local/gradle"
ENV PATH="${PATH}:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/tools:${GRADLE_HOME}/bin:${JAVA_HOME}"

RUN dpkg --add-architecture i386

RUN apt-get update

# Need these for adding Java 8 apt repo
RUN apt-get install -qy software-properties-common python-software-properties

RUN add-apt-repository ppa:webupd8team/java -y

RUN apt-get update

# Select the correct options for Java installation
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" | /usr/bin/debconf-set-selections
RUN echo "debconf shared/accepted-oracle-license-v1-1 seen true" | /usr/bin/debconf-set-selections
RUN echo "oracle-java7-installer shared/accepted-oracle-license-v1-1 select true" | /usr/bin/debconf-set-selections

RUN apt-get install -qy \
	libc6:i386 libstdc++6:i386 lib32z1 libsdl1.2debian:i386 \
	git-core curl unzip \
	oracle-java7-installer oracle-java8-installer

# Download and install upshift
RUN curl -fsSL https://raw.githubusercontent.com/leftshifters/upshift/master/upshift > upshift.temp && chmod +x upshift.temp && ./upshift.temp install

VOLUME ["/usr/local/android-sdk-linux", "/usr/local/gradle", "/builds"]
