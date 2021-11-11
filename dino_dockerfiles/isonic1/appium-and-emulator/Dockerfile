FROM ubuntu:14.04
MAINTAINER isonic1

RUN apt-get update
RUN apt-get install -y wget

# install Android SDK Appium dependencies
RUN apt-get install -y openjdk-7-jre-headless lib32z1 lib32ncurses5 lib32bz2-1.0 g++-multilib
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:chris-lea/node.js
RUN apt-get -y install nodejs

#create user
RUN useradd -m -s /bin/bash automator
USER automator
    
# Main Android SDK in user dir
RUN wget -qO- "http://dl.google.com/android/android-sdk_r23.0.2-linux.tgz" | tar -zxv -C /home/automator
RUN echo y | /home/automator/android-sdk-linux/tools/android update sdk --no-ui --all --filter platform-tools,build-tools-19.1.0,system-image,android-19,extra-android-support --force
ENV ANDROID_HOME /home/automator/android-sdk-linux
ENV ANDROID_SDK_HOME /home/automator/.android
RUN echo no | /home/automator/android-sdk-linux/tools/android create avd --force -n ANDROID -t android-19 --abi default/x86 --skin "HVGA"

RUN mkdir /home/automator/appium
ENV HOME /home/automator/appium
RUN cd /home/automator/appium && npm install appium

#Open appium port, start and wait for emulator, start appium server
EXPOSE 4723
CMD (/home/automator/android-sdk-linux/tools/emulator -verbose -avd ANDROID -no-skin -no-audio -no-window&) && sleep 30 && /home/automator/appium/node_modules/appium/bin/appium.js --device-ready-timeout 180
