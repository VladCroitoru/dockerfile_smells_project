FROM openjdk:8

ENV DEBIAN_FRONTEND noninteractive

# Install dependencies
RUN dpkg --add-architecture i386 && \
    apt-get -qq update && \
    apt-get -qqy install --no-install-recommends \
    libc6:i386 libstdc++6:i386 zlib1g:i386 libncurses5:i386 tar git curl && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

# Everything will be installed in the directory but jdk.
ENV SDK_HOME /usr/local

# Download and unzip Gradle
ENV GRADLE_VERSION 4.1
ENV GRADLE_SDK_URL https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip

RUN curl -sSL "${GRADLE_SDK_URL}" -o gradle-${GRADLE_VERSION}-bin.zip  \
	&& unzip gradle-${GRADLE_VERSION}-bin.zip -d ${SDK_HOME}  \
	&& rm -rf gradle-${GRADLE_VERSION}-bin.zip
ENV GRADLE_HOME ${SDK_HOME}/gradle-${GRADLE_VERSION}
ENV PATH ${GRADLE_HOME}/bin:$PATH

# Download and unzip Android SDK
ENV ANDROID_HOME ${SDK_HOME}/android-sdk-linux
ENV ANDROID_SDK ${SDK_HOME}/android-sdk-linux
ENV ANDROID_SDK_MANAGER ${SDK_HOME}/android-sdk-linux/tools/bin/sdkmanager

ENV ANDROID_SDK_VERSION sdk-tools-linux-3859397.zip
ENV ANDROID_SDK_URL https://dl.google.com/android/repository/${ANDROID_SDK_VERSION}

RUN curl -sSL "${ANDROID_SDK_URL}" -o ${ANDROID_SDK_VERSION} \
	&& unzip ${ANDROID_SDK_VERSION} -d ${ANDROID_HOME} \
	&& rm -rf ${ANDROID_SDK_VERSION}
  
ENV PATH ${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:$ANDROID_HOME/platform-tools:$PATH

RUN (while sleep 3; do echo "y"; done) | sdkmanager --update && (while sleep 3; do echo "y"; done) | sdkmanager --licenses

# Install Android SDK Components
ENV ANDROID_COMPONENTS "tools" \
                       "platform-tools" \
                       "build-tools;26.0.2" \
		       "build-tools;25.0.3" \
                       "platforms;android-25" \
                       "platforms;android-26"

ENV GOOGLE_COMPONENTS "extras;android;m2repository" \
                      "extras;google;m2repository" \
                      "extras;google;google_play_services" 
                       
ENV CONSTRAINT_LAYOUT "extras;m2repository;com;android;support;constraint;constraint-layout;1.0.0-beta4" \ 
"extras;m2repository;com;android;support;constraint;constraint-layout-solver;1.0.0-beta4" \
"extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2" \
"extras;m2repository;com;android;support;constraint;constraint-layout-solver;1.0.2"

RUN mkdir -p ${ANDROID_HOME}/licenses/ && \
    echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > ${ANDROID_HOME}/licenses/android-sdk-license && \
    echo "d56f5187479451eabf01fb78af6dfcb131a6481e" >> ${ANDROID_HOME}/licenses/android-sdk-license && \
    echo "84831b9409646a918e30573bab4c9c91346d8abd" > ${ANDROID_HOME}/licenses/android-sdk-preview-license && \
    (while sleep 3; do echo "y"; done) | ${ANDROID_SDK_MANAGER} ${ANDROID_COMPONENTS} \
                            ${GOOGLE_COMPONENTS} \
                            ${CONSTRAINT_LAYOUT}  

ENV ANDROID_NDK_COMPONENTS "ndk-bundle" \
                       "lldb;2.3" \
                       "cmake;3.6.4111459"
                       
RUN (while sleep 3; do echo "y"; done) | ${ANDROID_SDK_MANAGER} ${ANDROID_NDK_COMPONENTS}  

ENV ANDROID_NDK_HOME ${ANDROID_SDK}/ndk-bundle
ENV PATH ${ANDROID_NDK_HOME}:$PATH

RUN apt-get -qq update && \
    apt-get -qqy install python-pip python-setuptools --no-install-recommends && \
    pip install awscli && \
    apt-get remove --purge -y python-pip python-setuptools && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*
