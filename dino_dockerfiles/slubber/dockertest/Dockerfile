FROM	ubuntu:12.04
MAINTAINER	Jussi Pollari

#Set up the environment variables
#ENV DEBIAN_FRONTEND="noninteractive"
ENV	ANDROID_HOME="/opt/android-sdk-linux"
ENV	JAVA_HOME="/usr/lib/jvm/java-7-openjdk-amd64"
ENV	GRADLE_HOME="/gradle-2.1"
ENV	PATH="$PATH:$ANDROID_HOME/tools"
ENV	PATH="$PATH:$ANDROID_HOME/platform-tools"
ENV	PATH="$PATH:/gradle-2.1/bin"
ENV	PATH="$PATH:/usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java"

#Install curl, unzip, OpenJDK, Android SDK and Gradle
RUN apt-get install sudo
RUN sudo apt-get update
RUN sudo apt-get install -y curl
RUN sudo apt-get install -y unzip
RUN sudo apt-get install -y openjdk-7-jdk
RUN cd /opt && curl -L -O http://dl.google.com/android/android-sdk_r24.0.2-linux.tgz && tar xf android-sdk_r24.0.2-linux.tgz
RUN curl -L -O https://services.gradle.org/distributions/gradle-2.1-bin.zip && unzip gradle-2.1-bin.zip

#Install 32bit libraries
RUN sudo apt-get install -y lib32z1
RUN sudo apt-get install -y lib32bz2-1.0
RUN sudo apt-get install -y lib32ncurses5
RUN sudo apt-get install -y lib32stdc++6

#Update Android SDK tools
RUN echo "y" | android update sdk -u --all --filter tools
RUN echo "y" | android update sdk -u --all --filter build-tools-21.0.2
RUN echo "y" | android update sdk -u  --filter platform-tools,android-21

#Install GIT
RUN sudo apt-get install -y git

#Cleanup
RUN rm opt/android-sdk_r24.0.2-linux.tgz gradle-2.1-bin.zip