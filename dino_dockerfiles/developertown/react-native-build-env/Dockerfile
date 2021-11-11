FROM node:6.9.1

# https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz



# Base OS and runtime environments
RUN \
     apt-get update \
  && apt-get install -y \
       openjdk-7-jdk

# Android Tools
ENV \
  ANDROID_SDK_VERSION=24.4.1 \
  ANDROID_HOME=/opt/android-sdk-linux
ENV \
  PATH=$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH
RUN \
     cd /opt \
  && ANDROID_SDK_ARCHIVE=android-sdk_r${ANDROID_SDK_VERSION}-linux.tgz \
  && wget -q https://dl.google.com/android/${ANDROID_SDK_ARCHIVE} \
  && tar xzf ${ANDROID_SDK_ARCHIVE} \
  && rm ${ANDROID_SDK_ARCHIVE}

# Android SDKs and Tools
COPY android_sdk_install.sh /opt
RUN \
     /opt/android_sdk_install.sh "Android SDK Build-tools, revision 23.0.1" \
  && /opt/android_sdk_install.sh "Android SDK Build-tools, revision 23.0.3" \
  && /opt/android_sdk_install.sh "SDK Platform Android 6.0, API 23, revision 3" \
  && /opt/android_sdk_install.sh "Android Support Repository, revision 39" \
  && /opt/android_sdk_install.sh "Google APIs, Android API 23, revision 1" \
  && /opt/android_sdk_install.sh "Google Play services, revision 37" \
  && /opt/android_sdk_install.sh "Google Repository, revision 38" \
  && chown -R root:root $ANDROID_HOME \
  && chmod +x $ANDROID_HOME/tools/android \
  && rm -f /opt/android_sdk_install.sh

#  - Android SDK runtime dependencies
RUN \
     apt-get install -y \
       lib32stdc++6 \
       lib32z1

# React Native Tools
RUN \
     npm install -g react-native-cli

RUN \
     adduser \
       --disabled-password \
       --shell /bin/bash \
       --gecos "App User" \
       app \
  && mkdir /home/app/.gradle \
  && mkdir /home/app/.npm \
  && mkdir /app \
  && chown -R app:app /home/app \
  && chown -R app:app /app

WORKDIR /app
USER app
