FROM bitriseio/docker-android:latest
ENV ANDROID_NDK_HOME /opt/android-ndk
ENV ANDROID_NDK_VERSION r10e
ENV ANDROID_SDK_TOOLS_PATCH_INSTALLER_URL https://dl.google.com/android/repository/tools_r25.2.2-linux.zip
# ------------------------------------------------------
# --- Install required tools
RUN apt-get update -qq && \
    apt-get clean && \
    apt-get install -y xvfb awscli
# ------------------------------------------------------
# --- Android NDK
# download
RUN mkdir /opt/android-ndk-tmp && \
    cd /opt/android-ndk-tmp && \
    wget -q https://dl.google.com/android/repository/android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip && \
# uncompress
    unzip -q android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip && \
# move to its final location
    mv ./android-ndk-${ANDROID_NDK_VERSION} ${ANDROID_NDK_HOME} && \
# remove temp dir
    cd ${ANDROID_NDK_HOME} && \
    rm -rf /opt/android-ndk-tmp
# add to PATH
ENV PATH ${PATH}:${ANDROID_NDK_HOME}
# ------------------------------------------------------
# --- Android SDK (newer ones don't work with Unity)
RUN cd /opt \
    && wget -q $ANDROID_SDK_TOOLS_PATCH_INSTALLER_URL -O android-sdk-tools-patch.zip \
    && unzip -q android-sdk-tools-patch.zip -d patch \
    && mv ${ANDROID_HOME}/tools ${ANDROID_HOME}/tools_original \
    && mv patch/tools ${ANDROID_HOME} \
    && rm -rf patch android-sdk-tools-patch.zip
# ------------------------------------------------------
# --- Cleanup and rev num
RUN apt-get clean autoclean && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*
ENV BITRISE_DOCKER_REV_NUMBER_ANDROID_NDK v2017_06_03
CMD bitrise -version
