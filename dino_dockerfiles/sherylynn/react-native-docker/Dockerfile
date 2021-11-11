# Pull base image.
FROM ubuntu:14.04
MAINTAINER Sherylynn <352281674@qq.com>

# Install base software packages
RUN apt-get update && \
    apt-get install software-properties-common \
    python-software-properties \
    wget \
    curl \
    git \
    build-essential \
    unzip -y && \
    apt-get clean


# ——————————
# Install Java.
# ——————————

RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer


# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle


# ——————————
# Installs i386 architecture required for running 32 bit Android tools
# ——————————

RUN dpkg --add-architecture i386 && \
    apt-get update -y && \
    apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoremove -y && \
    apt-get clean


# ——————————
# Installs Android SDK
# ——————————

ENV ANDROID_SDK_VERSION r24.4.1
ENV ANDROID_SDK_FILENAME android-sdk_${ANDROID_SDK_VERSION}-linux.tgz
ENV ANDROID_SDK_URL http://dl.google.com/android/${ANDROID_SDK_FILENAME}

ENV ANDROID_BUILD_TOOLS_VERSION build-tools-24.0.1,build-tools-24,build-tools-23.0.3,build-tools-23.0.2,build-tools-23.0.1
# ————————————————————————————
#ENV ANDROID_TOOLS_VERSION r25.2.2
#ENV ANDROID_TOOLS_FILENAME tools_${ANDROID_TOOLS_VERSION}-linux.zip
#ENV ANDROID_TOOLS_URL https://dl.google.com/android/repository/${ANDROID_TOOLS_FILENAME}
#ENV ANDROID_PLATFORM_VERSION r24
#ENV ANDROID_PLATFORM_FILENAME platform-tools_${ANDROID_PLATFORM_VERSION}-linux.zip
#ENV ANDROID_PLATFORM_URL https://dl.google.com/android/repository/${ANDROID_PLATFORM_FILENAME}
# —————————————————————————————

ENV ANDROID_API_LEVELS android-23
ENV ANDROID_EXTRA_COMPONENTS extra-android-m2repository,extra-google-m2repository
ENV ANDROID_HOME /opt/android-sdk-linux
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools
RUN cd /opt && \
    wget -q ${ANDROID_SDK_URL} && \
    tar -xzf ${ANDROID_SDK_FILENAME} && \
    rm ${ANDROID_SDK_FILENAME} && \
#    wget -q ${ANDROID_TOOLS_URL} && \
#    unzip -n ${ANDROID_TOOLS_FILENAME} -d android-sdk-linux/tools && \
#    rm ${ANDROID_TOOLS_FILENAME} && \
#    wget -q ${ANDROID_PLATFORM_URL} && \
#    unzip -n ${ANDROID_PLATFORM_FILENAME} -d  && \
#    rm ${ANDROID_PLATFORM_FILENAME} && \

    echo y | android update sdk --no-ui -a --filter tools,platform-tools,${ANDROID_API_LEVELS},${ANDROID_BUILD_TOOLS_VERSION} && \
    echo y | android update sdk --no-ui --all --filter "${ANDROID_EXTRA_COMPONENTS}"

# ——————————
# Installs Android NDK
# ——————————

ENV ANDROID_NDK_VERSION r12b
ENV ANDROID_NDK_FILENAME android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip
ENV ANDROID_NDK_URL https://dl.google.com/android/repository/${ANDROID_NDK_FILENAME}
ENV ANDROID_NDK_HOME /opt/android-ndk-${ANDROID_NDK_VERSION}
ENV PATH ${ANDROID_NDK_HOME}:$PATH

RUN cd /opt && \
    wget -q ${ANDROID_NDK_URL} && \
    unzip  ${ANDROID_NDK_FILENAME} && \
    rm ${ANDROID_NDK_FILENAME}


# ——————————
# Installs Gradle
# ——————————

# Gradle
ENV GRADLE_VERSION 2.14.1

RUN cd /usr/lib \
 && curl -fl https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o gradle-bin.zip \
 && unzip "gradle-bin.zip" \
 && ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle \
 && rm "gradle-bin.zip"

# Set Appropriate Environmental Variables
ENV GRADLE_HOME /usr/lib/gradle
ENV PATH $PATH:$GRADLE_HOME/bin


# ——————————
# Install Node and global packages
# ——————————
ENV NODE_VERSION 5.10.1
RUN cd && \
    wget -q http://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz && \
    tar -xzf node-v${NODE_VERSION}-linux-x64.tar.gz && \
    mv node-v${NODE_VERSION}-linux-x64 /opt/node && \
    rm node-v${NODE_VERSION}-linux-x64.tar.gz
ENV PATH ${PATH}:/opt/node/bin


# ——————————
# Install Basic React-Native packages
# ——————————
RUN npm install react-native-cli -g
RUN npm install rnpm -g
RUN npm install react-native-update-cli -g
ENV LANG en_US.UTF-8