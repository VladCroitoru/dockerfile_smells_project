FROM openjdk:8-jdk

ENV SDK_HOME /opt

WORKDIR $SDK_HOME

# Dependencies for other things, like rust, clang, ndk, sdk, etc.
RUN apt-get --quiet update --yes
RUN apt-get --quiet install --yes wget tar unzip lib32stdc++6 lib32z1 git build-essential curl file g++ cmake pkg-config \
                        libasound2-dev bison flex unzip ant \
                        libncurses5 libclang-dev python clang --no-install-recommends

# Rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain nightly-2021-09-04 -t armv7-linux-androideabi aarch64-linux-android i686-linux-android x86_64-linux-android
ENV PATH /root/.cargo/bin:$PATH

# Gradle
ENV GRADLE_VERSION 6.7.1
ENV GRADLE_SDK_URL https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip
RUN curl -sSL "${GRADLE_SDK_URL}" -o gradle-${GRADLE_VERSION}-bin.zip  \
	&& unzip gradle-${GRADLE_VERSION}-bin.zip -d ${SDK_HOME}  \
	&& rm -rf gradle-${GRADLE_VERSION}-bin.zip
ENV GRADLE_HOME ${SDK_HOME}/gradle-${GRADLE_VERSION}
ENV PATH ${GRADLE_HOME}/bin:$PATH

# android sdk|build-tools|image
ENV ANDROID_TARGET_SDK="android-24,android-25" \
    ANDROID_BUILD_TOOLS="build-tools-24.0.2,build-tools-24.0.3,build-tools-25.0.2,build-tools-29.0.2" \
    ANDROID_SDK_TOOLS="25.2.3" \
    ANDROID_IMAGES="sys-img-armeabi-v7a-android-23,sys-img-armeabi-v7a-android-24"
ENV ANDROID_HOME ${SDK_HOME}/android-sdk-linux

RUN mkdir ${ANDROID_HOME} && wget --quiet --output-document=android-sdk.zip https://dl.google.com/android/repository/tools_r${ANDROID_SDK_TOOLS}-linux.zip && \
    unzip android-sdk.zip -d ${ANDROID_HOME}

ENV PATH ${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:$PATH

# Android Cmake
RUN wget -q https://dl.google.com/android/repository/cmake-3.6.3155560-linux-x86_64.zip -O android-cmake.zip
RUN unzip -q android-cmake.zip -d ${ANDROID_HOME}/cmake
ENV PATH ${PATH}:${ANDROID_HOME}/cmake/bin
RUN chmod u+x ${ANDROID_HOME}/cmake/bin/ -R

RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter "${ANDROID_TARGET_SDK}" && \
    echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter platform-tools && \
    echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter "${ANDROID_BUILD_TOOLS}"
# Idk if all this is needed but it seems to mess with maven so irdk what to do with it if you wanna take a deeper look kuai
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter extra-android-m2repository && \
    echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter extra-google-google_play_services && \
    echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter extra-google-m2repository

# Android NDK
RUN mkdir ${SDK_HOME}/android-sdk-linux/ndk && mkdir ${SDK_HOME}/android-sdk-linux/ndk/21.1.6352462

ENV ANDROID_NDK_VERSION r21d
ENV ANDROID_NDK_URL http://dl.google.com/android/repository/android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip
RUN curl -L "${ANDROID_NDK_URL}" -o android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip

RUN unzip android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip -d ${SDK_HOME}/android-sdk-linux/ndk/
RUN mv ${SDK_HOME}/android-sdk-linux/ndk/android-ndk-r21d/* ${SDK_HOME}/android-sdk-linux/ndk/21.1.6352462/
RUN rm -rf android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip
ENV ANDROID_NDK_ROOT ${SDK_HOME}/android-sdk-linux/ndk/21.1.6352462
ENV PATH ${ANDROID_NDK_ROOT}:$PATH
RUN chmod u+x ${ANDROID_NDK_ROOT}/ -R

RUN mkdir ${ANDROID_HOME}/licenses && echo "8933bad161af4178b1185d1a37fbf41ea5269c55" >> ${ANDROID_HOME}/licenses/android-sdk-license

## ADDITIONAL STEPS HERE
# I forgot to accept licenses :p
RUN yes | $ANDROID_HOME/tools/bin/sdkmanager "build-tools;29.0.2"
RUN yes | $ANDROID_HOME/tools/bin/sdkmanager "platforms;android-29"

# making the application folder
RUN mkdir /application
WORKDIR /application