###################################
# Dockerfile for jenkins-android ##
# Based on Ubuntu                ##
###################################

# Set the base image to Ubuntu
FROM ubuntu:16.04
MAINTAINER Chamunks <Chamunks@gmail.com>

# Never ask for confirmations
ENV DEBIAN_FRONTEND noninteractive
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" | /usr/bin/debconf-set-selections && \
    echo "debconf shared/accepted-oracle-license-v1-1 seen true" | /usr/bin/debconf-set-selections

# Add oracle-jdk6 packages to and from apt.
RUN apt-get update && \
    apt-get install software-properties-common python-software-properties -y && \
    add-apt-repository ppa:webupd8team/java && \
    apt-get update && \
    apt-get install oracle-java8-installer -y && \
    apt-get install oracle-java8-set-default -y && \
    apt-get install -y unzip && \
    apt-get install -y lib32ncurses5 lib32z1 && \
    apt-get autoclean -y && \
    apt-get autoremove -y

ENV JAVA_HOME /usr/bin/java
ENV PATH $JAVA_HOME:$PATH

# Add Android SDK
## Source https://developer.android.com/studio/index.html
RUN wget --progress=dot:giga https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && \
    mv android-sdk_r24.4.1-linux.tgz /opt/ && \
    cd /opt && tar xzvf ./android-sdk_r24.4.1-linux.tgz && \
    rm -r /opt/android-sdk_r24.4.1-linux.tgz && \
    apt-get install gcc-multilib -y && \
    apt-get autoclean -y && \
    apt-get autoremove -y
ENV ANDROID_HOME /opt/android-sdk-linux/
ENV PATH $ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH
RUN echo $PATH && \
    ( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) | android update sdk -u --filter platform-tools,android-19,build-tools-19.0.3 && \
    chmod -R 755 $ANDROID_HOME

# Add gradle
## Source https://services.gradle.org/distributions/
ADD https://services.gradle.org/distributions/gradle-2.14.1-bin.zip /opt/
RUN unzip /opt/gradle-2.14.1-bin.zip -d /opt && \
    rm /opt/gradle-2.14.1-bin.zip
ENV GRADLE_HOME /opt/gradle-2.14.1
ENV PATH $GRADLE_HOME/bin:$PATH

# Add git
RUN apt-get install -y git-core && \
    apt-get autoclean -y && \
    apt-get autoremove -y

# Add Jenkins
# Thanks to orchardup/jenkins Dockerfile
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add - && \
    echo "deb http://pkg.jenkins-ci.org/debian-stable binary/" >> /etc/apt/sources.list && \
    apt-get update && \
    mkdir /var/run/jenkins && \
    apt-get install -y jenkins && \
    service jenkins stop && \
    apt-get autoclean -y && \
    apt-get autoremove -y
EXPOSE 8080
VOLUME ["/root/.jenkins/"]
ENTRYPOINT [ "java","-jar","/usr/share/jenkins/jenkins.war" ]
