FROM openjdk:8-jdk

ENV ANDROID_COMPILE_SDK="27" ANDROID_BUILD_TOOLS="27.0.3" ANDROID_SDK_TOOLS="3859397" ANDROID_HOME="/opt" PATH="/opt/node/bin:/opt/tools:/opt/tools/bin:${PATH}"

RUN apt-get --quiet update --yes && \
    apt-get --quiet install --yes wget tar unzip lib32stdc++6 lib32z1 gradle apt-transport-https && \
    apt remove --yes cmdtest && \
    apt-get clean && cd /opt && \
    wget --quiet --output-document=android-sdk.zip https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_TOOLS}.zip && \
    unzip android-sdk.zip && rm android-sdk.zip && ls tools && \
    yes | sdkmanager --licenses && \ 
    touch ~/.android/repositories.cfg && \
    sdkmanager "emulator" "platform-tools" "platforms;android-${ANDROID_COMPILE_SDK}" "extras;google;google_play_services" "extras;google;m2repository" "extras;android;m2repository" "tools" "ndk-bundle" "build-tools;$ANDROID_BUILD_TOOLS" "system-images;android-${ANDROID_COMPILE_SDK};google_apis;x86"  && \
    echo yes | sdkmanager --licenses 
