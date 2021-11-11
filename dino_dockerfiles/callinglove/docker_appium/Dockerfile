############################################################
# Dockerfile to run appium for android devices
# learn from :
# 1、https://hub.docker.com/r/davidbaena/appium/~/dockerfile/
# 2、https://hub.docker.com/r/aluedeke/appium-android/~/dockerfile/
############################################################

FROM ubuntu:14.04
MAINTAINER callinglove

RUN apt-get update
RUN apt-get install -y wget maven curl build-essential usbutils

# install Android SDK dependencies
RUN apt-get install -y openjdk-7-jre-headless lib32z1 lib32ncurses5 lib32bz2-1.0 g++-multilib
    
# Main Android SDK
RUN wget -qO- "http://dl.google.com/android/android-sdk_r23.0.2-linux.tgz" | tar -zxv -C /opt/
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --all --filter platform-tools,build-tools-20.0.0 --no-ui --force

ENV ANDROID_HOME /opt/android-sdk-linux

RUN mkdir /opt/appium
RUN useradd -m -s /bin/bash appium
RUN chown -R appium:appium /opt/appium

USER appium
ENV HOME /home/appium

WORKDIR /opt/appium

RUN  mkdir .local && mkdir node
RUN curl http://nodejs.org/dist/node-latest.tar.gz | tar xz --strip-components=1
RUN ./configure --prefix=.local && make install

ENV NODE_PATH=/opt/appium/.local/lib/node_modules
ENV PATH=/opt/appium/.local/bin:$PATH

USER root
# Expose bin to default nodejs bin for sublime plugins
RUN ln -s /opt/appium/.local/bin/node  /usr/bin/nodejs
RUN ln -s /opt/appium/.local/lib/node_modules /usr/local/lib/

ENV appium_args "-p 4723"

USER appium
#Install npm
RUN curl -O https://npmjs.com/install.sh | sh

ENV appium_version 1.4.10
#Install appium
RUN npm install -g appium@${appium_version}


ADD files/insecure_shared_adbkey /home/appium/.android/adbkey
ADD files/insecure_shared_adbkey.pub /home/appium/.android/adbkey.pub

USER root
RUN apt-get -y install supervisor
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN $ANDROID_HOME/platform-tools/adb kill-server
RUN $ANDROID_HOME/platform-tools/adb start-server
RUN $ANDROID_HOME/platform-tools/adb devices
EXPOSE 22
CMD ["/usr/bin/supervisord"]
