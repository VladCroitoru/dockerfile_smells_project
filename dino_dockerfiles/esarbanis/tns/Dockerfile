FROM java 

MAINTAINER Efthymios Sarmpanis


RUN apt-get update && apt-get install -y lib32stdc++6 lib32z1 lib32ncurses5 g++ ant python make

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get install -y nodejs

# download and extract android sdk
RUN curl http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz | tar xz -C /usr/local/
ENV ANDROID_HOME /usr/local/android-sdk-linux
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

# update and accept licences
RUN ( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) | /usr/local/android-sdk-linux/tools/android update sdk --no-ui -a --filter platform-tool,extra-android-support,extra-android-m2repository,build-tools-23.0.1,android-23

RUN npm install -g nativescript

ENV GRADLE_USER_HOME /src/gradle
VOLUME /src
wORKDIR /src
