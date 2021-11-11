FROM ubuntu:16.10
MAINTAINER Tanya Kozel <sankleta@gmail.com>

RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y curl

RUN apt-get install -y openjdk-8-jre-headless
    
RUN curl "https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz" | tar -zxv -C /opt/
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --all --filter platform-tools,build-tools-25.0.0 --no-ui --force

ENV ANDROID_HOME /opt/android-sdk-linux
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
ENV PATH $PATH:/usr/lib/jvm/java-8-openjdk-amd64/bin

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs

RUN npm install appium-adb@2.7.0
RUN npm install appium@1.6.0
RUN npm install appium-doctor@1.2.5

EXPOSE 4723
CMD /node_modules/appium/build/lib/main.js