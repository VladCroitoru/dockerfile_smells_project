FROM centos

MAINTAINER Sanchit <gupta.sanchit90@outlook.com>

# Epel
# RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm

# Install Development Tools
RUN yum -y groupinstall "Development Tools"

# yum update
RUN yum -y update

# Install java (OpenJDK)
RUN yum -y install java-1.7.0-openjdk-devel

# Install Expect
RUN yum -y install expect

# Install 32bit Library
RUN yum -y install glibc.i686
RUN yum -y install libstdc++.i686
RUN yum -y install glibc-devel.i686
RUN yum -y install zlib-devel.i686
RUN yum -y install ncurses-devel.i686
RUN yum -y install libX11-devel.i686
RUN yum -y install libXrender.i686

# Install Android SDK
RUN cd /usr/local/ && curl -L -O http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && tar xf android-sdk_r24.4.1-linux.tgz

# Install Android tools
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui --force -a --filter tools 
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui --force -a --filter platform-tools 
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui --force -a --filter build-tools-23.0.2 
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui --force -a --filter android-23 
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui --force -a --filter android-15 
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui --force -a --filter extra 

# Install Gradle
RUN cd /usr/local/ && curl -L -O http://services.gradle.org/distributions/gradle-2.10-all.zip && unzip -o gradle-2.10-all.zip

# Environment variables
ENV ANDROID_HOME /usr/local/android-sdk-linux
ENV GRADLE_HOME /usr/local/gradle-2.10
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk

ENV PATH $PATH:$ANDROID_HOME/tools
ENV PATH $PATH:$ANDROID_HOME/platform-tools
ENV PATH $PATH:$GRADLE_HOME/bin

# Clean up
RUN rm -rf /usr/local/android-sdk_r24.4.1-linux.tgz
RUN rm -rf /usr/local/gradle-2.10-all.zip
RUN yum clean all

