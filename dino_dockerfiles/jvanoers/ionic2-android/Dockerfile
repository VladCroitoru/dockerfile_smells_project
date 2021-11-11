FROM gradle:3.5-jdk8

USER root

# Node 7
# Installs i386 architecture required for running 32 bit Android tools
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && \
    dpkg --add-architecture i386 \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        nodejs \
        libc6:i386 \
        libncurses5:i386 \
        libstdc++6:i386 \
        zlib1g:i386 \
        lib32gcc1 \
        lib32z1 \
        lib32stdc++6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install android SDK, tools and platforms
RUN cd /opt \
    && curl https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz -o android-sdk.tgz \
    && tar xzf android-sdk.tgz \
    && rm android-sdk.tgz

ENV ANDROID_HOME /opt/android-sdk-linux
RUN echo 'y' | /opt/android-sdk-linux/tools/android update sdk -u -a -t \
    platform-tools,build-tools-25.0.2,android-25,extra-google-google_play_services,extra-google-m2repository,extra-android-m2repository

# Install npm packages
RUN npm i -g cordova ionic gulp bower grunt phonegap node-gyp

# Create dummy app to build and preload gradle and maven dependencies
RUN cd / \
    && echo 'n' | ionic start app blank --no-git --skip-link --cordova \
    && cd /app \
    && ionic cordova platform add android \
    && ionic cordova build android \
    && rm -rf * .??*

WORKDIR /app
