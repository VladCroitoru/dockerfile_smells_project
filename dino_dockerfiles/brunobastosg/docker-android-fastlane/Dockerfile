FROM openjdk:8

ENV ANDROID_HOME /opt/android-sdk-linux

# Download Android SDK into $ANDROID_HOME
# You can find URL to the current version at: https://developer.android.com/studio/index.html

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools

RUN mkdir -p ${ANDROID_HOME} && \
    cd ${ANDROID_HOME} && \
    wget -q https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip -O android_tools.zip && \
    unzip android_tools.zip && \
    rm android_tools.zip &&  \
    yes | sdkmanager --licenses && \
    sdkmanager 'platform-tools' && \
    sdkmanager 'platforms;android-28' && \
    sdkmanager 'build-tools;28.0.3' && \
    sdkmanager 'extras;m2repository;com;android;support;constraint;constraint-layout-solver;1.0.2' && \
    sdkmanager 'extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2' && \
    sdkmanager 'extras;google;m2repository' && \
    sdkmanager 'extras;android;m2repository' && \
    sdkmanager 'extras;google;google_play_services' && \
    apt-get update &&  apt-get install --no-install-recommends -y build-essential ca-certificates  git ruby2.3-dev \
    && update-ca-certificates \
    && gem install fastlane \
    && gem install bundler \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && apt-get autoremove -y && apt-get clean



