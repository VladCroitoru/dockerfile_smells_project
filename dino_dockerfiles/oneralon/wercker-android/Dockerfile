FROM debian:jessie
MAINTAINER oneralon <oneralon@gmail.com>

RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list && \
    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && apt-get update -y && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    apt-get install -y unzip curl oracle-java8-installer && rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/oracle-jdk8-installer && \
    cd /usr/local/ && curl -L -O http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && tar xf android-sdk_r24.4.1-linux.tgz && \
    echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui --force --all --filter "tools" && \
    echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui --force --all --filter "platform-tools,build-tools-24.0.0,build-tools-23.0.3,build-tools-23.0.2,android-24,android-23,android-19" && \
    echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui --force --all --filter "extra-google-google_play_services,extra-google-m2repository,extra-android-m2repository,extra-android-support,addon-google_apis-google-23" && \
    cd /usr/local/ && curl -L -O https://services.gradle.org/distributions/gradle-2.14-all.zip && unzip -o gradle-2.14-all.zip && \
    rm -rf /usr/local/android-sdk_r24.4.1-linux.tgz && rm -rf /usr/local/gradle-2.14-all.zip

ENV ANDROID_HOME /usr/local/android-sdk-linux
ENV GRADLE_HOME /usr/local/gradle-2.14
ENV PATH $PATH:$ANDROID_HOME/tools
ENV PATH $PATH:$ANDROID_HOME/platform-tools
ENV PATH $PATH:$GRADLE_HOME/bin
