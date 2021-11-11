FROM openjdk:8-jdk

ENV ANDROID_HOME /opt/android-sdk-linux
ENV GRADLE_PATH /opt/gradle-4.10

RUN dpkg --add-architecture i386 && \
    apt-get update -y && \
    apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 build-essential && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoremove -y && \
    apt-get clean

RUN cd /opt \
    && wget -q https://dl.google.com/android/repository/tools_r25.2.5-linux.zip -O android-sdk-tools.zip \
    && unzip -q android-sdk-tools.zip -d ${ANDROID_HOME} \
    && rm -f android-sdk-tools.zip

RUN cd /opt \
    && wget -q https://downloads.gradle.org/distributions/gradle-4.10-bin.zip -O gradle.zip \
    && unzip -q gradle.zip \
    && rm -f gradle.zip

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/build-tools/25.0.2:${GRADLE_PATH}/bin

# Due to new agreement
RUN echo 'y' | android update sdk --no-ui --all --filter "extra-android-m2repository"

# ------------------------------------------------------
# --- Install Android SDKs and other build packages

# Other tools and resources of Android SDK
#  you should only install the packages you need!
# To get a full list of available options you can use:
#  sdkmanager --list

# Accept "android-sdk-license" before installing components, no need to echo y for each component
# License is valid for all the standard components in versions installed from this file
# Non-standard components: MIPS system images, preview versions, GDK (Google Glass) and Android Google TV require separate licenses, not accepted there
RUN mkdir -p ${ANDROID_HOME}/licenses
RUN echo -e "8933bad161af4178b1185d1a37fbf41ea5269c55\n\nd56f5187479451eabf01fb78af6dfcb131a6481e\n\n24333f8a63b6825ea9c5514f83c2829b004d1fee" > ${ANDROID_HOME}/licenses/android-sdk-license

# Platform tools
RUN echo 'y' | sdkmanager "platform-tools"

# SDKs
# Please keep these in descending order!
RUN echo 'y' | sdkmanager "platforms;android-26"

# build tools
# Please keep these in descending order!
RUN echo 'y' | sdkmanager "build-tools;25.0.2"

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs && \
    npm update -g npm && \
    npm install -g ionic@4 cordova@8 && \
    npm cache --force clean
