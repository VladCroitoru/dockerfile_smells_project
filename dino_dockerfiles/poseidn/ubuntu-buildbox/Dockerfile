FROM ubuntu:16.10

RUN apt-get update -qq && apt-get dist-upgrade -y

RUN apt-get install -y \
    build-essential iwyu cmake g++ \
    libglm-dev libglew-dev libboost-all-dev freeglut3-dev \
    libsdl2-image-dev libsdl2-dev \ 
    wget default-jre unzip \
    doxygen graphviz

# Installs Android SDK
ENV ANDROID_SDK_FILENAME android-sdk_r24.4.1-linux.tgz
ENV ANDROID_SDK_URL http://dl.google.com/android/${ANDROID_SDK_FILENAME}
ENV ANDROID_API_LEVELS android-18,android-19,android-20,android-21,android-22,android-23,android-24
ENV ANDROID_BUILD_TOOLS_VERSION 24.0.2
ENV ANDROID_HOME /opt/android-sdk-linux
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools
RUN cd /opt && \
    wget -q ${ANDROID_SDK_URL} && \
    tar -xzf ${ANDROID_SDK_FILENAME} && \
    rm ${ANDROID_SDK_FILENAME} && \
    echo y | android update sdk --no-ui -a --filter tools,platform-tools,${ANDROID_API_LEVELS},build-tools-${ANDROID_BUILD_TOOLS_VERSION}

# Install the Android NDK
ENV ANDROID_NDK_FILENAME android-ndk-r13b-linux-x86_64.zip
ENV ANDROID_NDK_URL https://dl.google.com/android/repository/${ANDROID_NDK_FILENAME}
ENV ANDROID_NDK_HOME /opt/android-ndk-r13b
ENV PATH ${PATH}:${ANDROID_NDK_HOME}
RUN cd /opt && \
    wget -q ${ANDROID_NDK_URL} && \
    unzip ${ANDROID_NDK_FILENAME} && \
    rm ${ANDROID_NDK_FILENAME}

