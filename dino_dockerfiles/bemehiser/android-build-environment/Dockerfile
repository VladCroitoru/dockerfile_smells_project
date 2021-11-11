FROM ubuntu:16.04

ENV DOCKER_ANDROID_LANG en_US
ENV DOCKER_ANDROID_DISPLAY_NAME mobileci-docker

ENV DEBIAN_FRONTEND noninteractive

RUN rm -rf /var/lib/apt/lists/* && \
    apt-get -q update && \
    apt-get -q full-upgrade -y

RUN apt-get install -q -y \
  autoconf \
  build-essential \
  bzip2 \
  curl \
  gcc \
  git \
  gperf \
  groff \
  lib32stdc++6 \
  lib32z1 \
  lib32z1-dev \
  lib32ncurses5 \
  libc6-dev \
  libgmp-dev \
  libmpc-dev \
  libmpfr-dev \
  libxslt-dev \
  libxml2-dev \
  m4 \
  make \
  ncurses-dev \
  ocaml \
  openssh-client \
  openjdk-8-jdk-headless\
  pkg-config \
  python-software-properties \
  rsync \
  ruby \
  software-properties-common \
  unzip \
  wget \
  zip \
  zlib1g-dev \
  --no-install-recommends

RUN rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Install CMake
RUN wget -q https://cmake.org/files/v3.10/cmake-3.10.2.tar.gz && \
    tar xzf cmake-3.10.2.tar.gz && \
    cd cmake-3.10.2 && \
    ./configure && \
    make && \
    make install && \
    cd .. && \
    rm -rf cmake-3.10.2.tar.gz cmake-3.10.2

# Install Go
RUN wget -q https://redirector.gvt1.com/edgedl/go/go1.9.2.linux-amd64.tar.gz && \
    tar xzf go1.9.2.linux-amd64.tar.gz && \
    mv go /usr/local/go && \
    ln -s /usr/local/go/bin/go /usr/local/bin/go && \
    rm go1.9.2.linux-amd64.tar.gz

# Install Android SDK Tools
RUN wget -q https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip && \
    unzip -q sdk-tools-linux-3859397.zip -d android-sdk && \
    mv android-sdk /usr/local/android-sdk && \
    rm sdk-tools-linux-3859397.zip
ENV PATH $PATH:/usr/local/android-sdk/tools/bin

# Accept license
RUN yes | sdkmanager --licenses

# Install Android SDK
RUN touch ~/.android/repositories.cfg && \
    sdkmanager --update && \
    sdkmanager "platform-tools" "build-tools;26.0.3" "platforms;android-26" "cmake;3.6.4111459"

# Install Android NDK
RUN wget -q http://dl.google.com/android/repository/android-ndk-r16b-linux-x86_64.zip && \
    unzip -q android-ndk-r16b-linux-x86_64.zip && \
    mv android-ndk-r16b /usr/local/android-ndk && \
    rm android-ndk-r16b-linux-x86_64.zip

# Environment variables
ENV ANDROID_HOME /usr/local/android-sdk
ENV ANDROID_SDK_HOME $ANDROID_HOME
ENV ANDROID_NDK_HOME /usr/local/android-ndk
ENV ANDROID_NDK_r16b $ANDROID_NDK_HOME
ENV PATH $PATH:/usr/local/go/bin
ENV GOPATH $HOME/go
ENV PATH $PATH:$GOPATH/bin
ENV JENKINS_HOME $HOME
ENV PATH ${INFER_HOME}/bin:${PATH}
ENV PATH $PATH:$ANDROID_SDK_HOME/tools
ENV PATH $PATH:$ANDROID_SDK_HOME/platform-tools
ENV PATH $PATH:$ANDROID_SDK_HOME/android-sdk/build-tools/26.0.3
ENV PATH $PATH:$ANDROID_NDK_HOME

# Export JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

# Gradle
ENV TERM dumb
ENV JAVA_OPTS "-Xms4096m -Xmx4096m"
ENV GRADLE_OPTS "-XX:+UseG1GC -XX:MaxGCPauseMillis=1000"

# Cleaning
RUN apt-get clean

# Add build user account, values are set to default below
ENV RUN_USER jenkins
ENV RUN_UID 8504

RUN id $RUN_USER || adduser --uid "$RUN_UID" \
    --gecos 'Build User' \
    --shell '/bin/sh' \
    --disabled-login \
    --disabled-password "$RUN_USER"

# Fix permissions
RUN chown -R $RUN_USER:$RUN_USER $ANDROID_HOME $ANDROID_SDK_HOME $ANDROID_NDK_HOME && \
    chmod -R a+rx $ANDROID_HOME $ANDROID_SDK_HOME $ANDROID_NDK_HOME

# Creating project directories prepared for build when running `docker run`
ENV PROJECT /project
RUN mkdir $PROJECT && \
    chown -R $RUN_USER:$RUN_USER $PROJECT
WORKDIR $PROJECT

USER $RUN_USER
RUN echo "sdk.dir=$ANDROID_HOME" > local.properties
