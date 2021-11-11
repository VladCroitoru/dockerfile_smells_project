FROM openjdk:8-jdk

LABEL maintainer "@tonymadbrain <anton.ryabov@onetwotrip.com>"

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -yq libstdc++6:i386 zlib1g:i386 libncurses5:i386 --no-install-recommends && \
    apt-get clean

ENV ANDROID_HOME /usr/local/android_sdk

RUN curl -sO "https://dl.google.com/android/repository/tools_r25.0.2-linux.zip" && \
    unzip -q tools_r25.0.2-linux.zip && \
    mkdir $ANDROID_HOME && \
    rm -f tools_r25.0.2-linux.zip && \
    mv tools $ANDROID_HOME/ 

ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

RUN (while :; do echo 'y'; sleep 3; done) | android update sdk --no-ui --all --filter platform-tools,build-tools-25.0.2,android-25,extra-android-m2repository,extra-android-support,extra-google-google_play_services,extra-google-m2repository

ENV JAVA_OPTS -Xms256m -Xmx512m
