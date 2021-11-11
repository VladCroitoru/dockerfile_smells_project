FROM debian:latest
MAINTAINER @FrenchYeti

RUN useradd -ms /bin/bash drozer

# Install all dependencies
RUN apt-get update && \
    apt-get install -y wget openjdk-7-jre-headless libc6-i386 lib32stdc++6 lib32z1 && \
    apt-get -y install bash-completion python2.7 python-dev python-protobuf python-openssl python-twisted && \
    apt-get clean && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install android tools + sdk
ENV ANDROID_HOME /opt/android-sdk-linux
ENV PATH $PATH:${ANDROID_HOME}/tools:$ANDROID_HOME/platform-tools

# Set up insecure default key
RUN mkdir -m 0750 /.android
ADD files/insecure_shared_adbkey /.android/adbkey
ADD files/insecure_shared_adbkey.pub /.android/adbkey.pub

RUN wget -qO- "http://dl.google.com/android/android-sdk_r24.3.4-linux.tgz" | tar -zx -C /opt && \
    echo y | android update sdk --no-ui --all --filter platform-tools --force

# Switch to drozer's home directory
WORKDIR /home/drozer

# Download the console
RUN wget -c 'https://github.com/mwrlabs/drozer/releases/download/2.3.4/drozer_2.3.4.deb'

# Install the console
RUN dpkg -i drozer_2.3.4.deb
RUN rm *.deb

# Run as drozer user
USER drozer

# Download agent
RUN wget -c 'https://github.com/mwrlabs/drozer/releases/download/2.3.4/drozer-agent-2.3.4.apk'

# Download sieve
RUN wget -c 'https://github.com/mwrlabs/drozer/releases/download/2.3.4/sieve.apk'

# Port forwarding required by drozer
RUN echo 'adb forward tcp:31415 tcp:31415' >> /home/drozer/.bashrc

