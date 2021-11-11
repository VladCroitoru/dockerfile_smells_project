#
# GitLab CI Android Runner
#
#
FROM openjdk:8-jdk

ENV ANDROID_BUILD_TOOLS "27.0.3"
ENV ANDROID_SDK_TOOLS "25.2.5"
ENV ANDROID_HOME "/android-sdk"
ENV ANDROID_VERSION "22"

# emulator is in its own path since 25.3.0 (not in sdk tools anymore)
ENV PATH=$PATH:${ANDROID_HOME}/emulator:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools

# Prepare dependencies
RUN mkdir $ANDROID_HOME \
  && apt-get update --yes \
  && apt-get install --yes wget tar unzip lib32stdc++6 lib32z1 libqt5widgets5 expect \
  && apt-get clean \
  && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install sdk tools
RUN wget -O android-sdk.zip https://dl.google.com/android/repository/tools_r${ANDROID_SDK_TOOLS}-linux.zip \
  && unzip -q android-sdk.zip -d $ANDROID_HOME \
  && rm android-sdk.zip

# Workaround for 
# Warning: File /root/.android/repositories.cfg could not be loaded.
RUN mkdir /root/.android \
  && touch /root/.android/repositories.cfg

# Workaround for host bitness error with android emulator
# https://stackoverflow.com/a/37604675/455578
RUN mv /bin/sh /bin/sh.backup \
  && cp /bin/bash /bin/sh

# Add tools from travis
ADD https://raw.githubusercontent.com/travis-ci/travis-cookbooks/ca800a93071a603745a724531c425a41493e70ff/community-cookbooks/android-sdk/files/default/android-wait-for-emulator /usr/local/bin/android-wait-for-emulator
RUN chmod +x /usr/local/bin/android-wait-for-emulator

# Add own tools
COPY assure_emulator_awake.sh /usr/local/bin/assure_emulator_awake.sh
RUN chmod +x /usr/local/bin/assure_emulator_awake.sh

# Update platform and build tools
RUN echo "y" | sdkmanager "tools" "platform-tools" "build-tools;${ANDROID_BUILD_TOOLS}"

# Update SDKs
RUN echo "y" | sdkmanager "platforms;android-${ANDROID_VERSION}"

# Update emulators
RUN echo "y" | sdkmanager "system-images;android-${ANDROID_VERSION};google_apis;armeabi-v7a" "system-images;android-${ANDROID_VERSION};google_apis;x86"

# Update extra
RUN echo "y" | sdkmanager "extras;android;m2repository" "extras;google;m2repository" "extras;google;google_play_services"

# Constraint Layout
RUN echo "y" | sdkmanager "extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2"
RUN echo "y" | sdkmanager "extras;m2repository;com;android;support;constraint;constraint-layout-solver;1.0.2"

RUN echo no | avdmanager -v create avd --force --name test --abi google_apis/armeabi-v7a --package "system-images;android-${ANDROID_VERSION};google_apis;armeabi-v7a"
RUN echo no | avdmanager -v create avd --force --name test86 --abi google_apis/x86 --package "system-images;android-${ANDROID_VERSION};google_apis;x86"

RUN wget -q --output-document=android-ndk.zip https://dl.google.com/android/repository/android-ndk-r16-linux-x86_64.zip && \
 	unzip android-ndk.zip && \
 	rm -f android-ndk.zip && \
 	mv android-ndk-r16 android-ndk-linux
 ENV ANDROID_NDK=$PWD/android-ndk-linux
 ENV ANDROID_NDK_HOME=$PWD/android-ndk-linux

# CMAKE KEEP V6 ONLY
# Needed for ToF but the emulator wont start
# RUN echo "y" | sdkmanager --uninstall "cmake;3.10.2.4988404"
# RUN echo "y" | sdkmanager "cmake;3.6.4111459"

# echo actually installed Android SDK packages
RUN sdkmanager --list
