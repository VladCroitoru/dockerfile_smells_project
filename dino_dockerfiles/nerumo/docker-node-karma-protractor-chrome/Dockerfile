FROM node:9.11.1

# Install Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list  && \
    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886

WORKDIR /usr/src/app

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    google-chrome-stable \
    curl \
    build-essential \
    expect \
    unzip \
    git \
    python \
    lib32stdc++6 lib32z1

RUN echo "===> install Java"  && \
    mkdir -p /usr/share/man/man1 && \
    echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections  && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections  && \
    DEBIAN_FRONTEND=noninteractive  apt-get install -y --force-yes oracle-java8-installer oracle-java8-set-default


RUN echo "===> clean up..."  && \
    rm -rf /var/cache/oracle-jdk8-installer  && \
    apt-get clean  && \
    rm -rf /var/lib/apt/lists/*

RUN npm i -g cordova@6.5.0

RUN curl http://dl.google.com/android/android-sdk_r24.2-linux.tgz | tar xz -C /usr/local/
ENV ANDROID_HOME /usr/local/android-sdk-linux
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

# update and accept licences
RUN (sleep 10 && while [ 1 ]; do sleep 2; echo y; done) |  android - update sdk --no-ui --filter platform-tool,build-tools-23.0.1,android-24

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
ENV PYTHON /usr/bin/python

RUN mkdir -p /src/gradle
RUN wget -P /tmp https://services.gradle.org/distributions/gradle-3.5-bin.zip 
RUN unzip /tmp/gradle-3.5-bin.zip  -d /src/gradle/
ENV PATH="/src/gradle/gradle-3.5/bin:${PATH}"

RUN mkdir /usr/local/android-sdk-linux/licenses
RUN echo "\n8933bad161af4178b1185d1a37fbf41ea5269c55" > $ANDROID_HOME/licenses/android-sdk-license
RUN echo "\nd56f5187479451eabf01fb78af6dfcb131a6481e" >> $ANDROID_HOME/licenses/android-sdk-license

ENV GRADLE_USER_HOME /src/gradle/gradle-3.5

CMD npm test
