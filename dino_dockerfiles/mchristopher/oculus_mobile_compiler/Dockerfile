# Docker container for Android / Oculus Compliation
# 
# Mike Christopher <mchristopher (at) gmail>
#

# Load Ubuntu by default
FROM ubuntu:trusty

# Install Java and 32-bit tools for compiling Android
RUN dpkg --add-architecture i386 && \
    apt-get update -y && \
    apt-get install -y software-properties-common libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 p7zip-full python build-essential dos2unix wget && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update -y && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer && \
    apt-get remove software-properties-common -y && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk8-installer/* && \
    rm -rf /usr/lib/jvm/java-8-oracle/*.zip && \
    apt-get autoremove -y && \
    apt-get clean

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Installs Android SDK & NDK
ENV ANDROID_API_LEVELS android-19,android-23
ENV ANDROID_BUILD_TOOLS_VERSION 22.0.1
ENV ANDROID_HOME /opt/android-sdk-linux
RUN cd /opt && \
    wget -q https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && \
    tar -xzf android-sdk_r24.4.1-linux.tgz && \
    rm android-sdk_r24.4.1-linux.tgz && \
    echo y | ${ANDROID_HOME}/tools/android update sdk --no-ui -a --filter tools,platform-tools,${ANDROID_API_LEVELS},build-tools-${ANDROID_BUILD_TOOLS_VERSION} && \
    rm -fr ~/.android && rm -fr ~/.oracle_jre_usage

# Installs Android NDK
# NOTE: Removes files not needed by Oculus SDK
ENV ANDROID_NDK_VERSION r10e
ENV ANDROID_NDK /opt/android-ndk-${ANDROID_NDK_VERSION}
RUN cd /opt && \
    wget -q https://dl.google.com/android/ndk/android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.bin && \
    7z x -y android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.bin > /dev/null && \
    rm android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.bin && \
    rm -fr /opt/android-ndk-r10e/docs && \
    rm -fr /opt/android-ndk-r10e/prebuilt/android-arm && \
    rm -fr /opt/android-ndk-r10e/prebuilt/android-arm64 && \
    rm -fr /opt/android-ndk-r10e/prebuilt/android-mips && \
    rm -fr /opt/android-ndk-r10e/prebuilt/android-mips64 && \
    rm -fr /opt/android-ndk-r10e/prebuilt/android-x86 && \
    rm -fr /opt/android-ndk-r10e/prebuilt/android-x86_64 && \
    rm -fr /opt/android-ndk-r10e/platforms/android-3 && \
    rm -fr /opt/android-ndk-r10e/platforms/android-4 && \
    rm -fr /opt/android-ndk-r10e/platforms/android-5 && \
    rm -fr /opt/android-ndk-r10e/platforms/android-8 && \
    rm -fr /opt/android-ndk-r10e/platforms/android-9 && \
    rm -fr /opt/android-ndk-r10e/platforms/android-12 && \
    rm -fr /opt/android-ndk-r10e/platforms/android-13 && \
    rm -fr /opt/android-ndk-r10e/platforms/android-14 && \
    rm -fr /opt/android-ndk-r10e/platforms/android-15 && \
    rm -fr /opt/android-ndk-r10e/platforms/android-16 && \
    rm -fr /opt/android-ndk-r10e/platforms/android-17 && \
    rm -fr /opt/android-ndk-r10e/platforms/android-18 && \
    rm -fr /opt/android-ndk-r10e/platforms/android-21 && \
    rm -fr /opt/android-ndk-r10e/samples && \
    rm -fr /opt/android-ndk-r10e/toolchains/aarch64-linux-android-4.9 && \
    rm -fr /opt/android-ndk-r10e/toolchains/aarch64-linux-android-clang3.5 && \
    rm -fr /opt/android-ndk-r10e/toolchains/aarch64-linux-android-clang3.6 && \
    rm -fr /opt/android-ndk-r10e/toolchains/arm-linux-androideabi-4.9 && \
    rm -fr /opt/android-ndk-r10e/toolchains/arm-linux-androideabi-clang3.5 && \
    rm -fr /opt/android-ndk-r10e/toolchains/arm-linux-androideabi-clang3.6 && \
    rm -fr /opt/android-ndk-r10e/toolchains/llvm-3.5 && \
    rm -fr /opt/android-ndk-r10e/toolchains/llvm-3.6 && \
    rm -fr /opt/android-ndk-r10e/toolchains/mips64el-linux-android-4.9 && \
    rm -fr /opt/android-ndk-r10e/toolchains/mips64el-linux-android-clang3.5 && \
    rm -fr /opt/android-ndk-r10e/toolchains/mips64el-linux-android-clang3.6 && \
    rm -fr /opt/android-ndk-r10e/toolchains/mipsel-linux-android-4.8 && \
    rm -fr /opt/android-ndk-r10e/toolchains/mipsel-linux-android-4.9 && \
    rm -fr /opt/android-ndk-r10e/toolchains/mipsel-linux-android-clang3.5 && \
    rm -fr /opt/android-ndk-r10e/toolchains/mipsel-linux-android-clang3.6 && \
    rm -fr /opt/android-ndk-r10e/toolchains/renderscript && \
    rm -fr /opt/android-ndk-r10e/toolchains/x86-4.8 && \
    rm -fr /opt/android-ndk-r10e/toolchains/x86-4.9 && \
    rm -fr /opt/android-ndk-r10e/toolchains/x86_64-4.9 && \
    rm -fr /opt/android-ndk-r10e/toolchains/x86_64-clang3.5 && \
    rm -fr /opt/android-ndk-r10e/toolchains/x86_64-clang3.6 && \
    rm -fr /opt/android-ndk-r10e/toolchains/x86-clang3.5 && \
    rm -fr /opt/android-ndk-r10e/toolchains/x86-clang3.6 && \
    rm -fr /opt/android-ndk-r10e/sources/android && \
    rm -fr /opt/android-ndk-r10e/sources/cpufeatures && \
    rm -fr /opt/android-ndk-r10e/sources/third_party && \
    rm -fr /opt/android-ndk-r10e/sources/cxx-stl/gnu-libstdc++/4.9 && \
    rm -fr /opt/android-ndk-r10e/sources/cxx-stl/llvm-libc++ && \
    rm -fr /opt/android-ndk-r10e/sources/cxx-stl/llvm-libc++abi && \
    rm -fr /opt/android-ndk-r10e/sources/cxx-stl/system

# Install Oculus SDK & pre-compile libraries
ENV OCULUS_SDK_VERSION 1.0.0.0
ENV OCULUS_SDK_HOME /opt/oculus-sdk
RUN mkdir -p ${OCULUS_SDK_HOME} && cd ${OCULUS_SDK_HOME} && \
    wget -q https://static.oculus.com/sdk-downloads/ovr_sdk_mobile_${OCULUS_SDK_VERSION}.zip && \
    7z x -y ovr_sdk_mobile_${OCULUS_SDK_VERSION}.zip > /dev/null && \
    touch ${OCULUS_SDK_HOME}/local.properties && \
    chmod a+x ${OCULUS_SDK_HOME}/gradlew && \
    dos2unix ${OCULUS_SDK_HOME}/gradlew && \
    dos2unix ${OCULUS_SDK_HOME}/*.py && \
    dos2unix ${OCULUS_SDK_HOME}/*.gradle && \
    dos2unix ${OCULUS_SDK_HOME}/*.mk && \
    ${OCULUS_SDK_HOME}/gradlew printProjectName && \
    cd ${OCULUS_SDK_HOME}/VrSamples/Native/VrTemplate/Projects/Android && \
    sed -i -- 's/VrGui/VrGUI/g' *.gradle && \
    sed -i -- 's/VrGui/VrGUI/g' jni/*.mk && \
    env PATH=${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${ANDROID_NDK} \
      python build.py -n -c --no-daemon release && \
    cd ${OCULUS_SDK_HOME} && \
    rm ovr_sdk_mobile_${OCULUS_SDK_VERSION}.zip && \
    rm -fr ${OCULUS_SDK_HOME}/SourceAssets && \
    rm -fr ${OCULUS_SDK_HOME}/sdcard_SDK && \
    rm -fr ${OCULUS_SDK_HOME}/VrSamples && \
    rm -fr ${OCULUS_SDK_HOME}/*.apk

# Update PATH variables
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${ANDROID_NDK}
