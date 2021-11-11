FROM ubuntu:16.04

ENV JDK_VERSION=8u131-b11-0ubuntu1.16.04.2 \
    ANDROID_SDK_TOOLS_VERSION=25 \
    ANDROID_BUILD_TOOLS_VERSION=25.0.3 \
    ANDROID_TARGET_SDK_VERSION=25 \
    ANDROID_HOME="/opt/android" \
    NODEJS_VERSION=6.10.0 \
    NODE_PATH="/opt/node" \
    REACT_NATIVE_CLI_VERSION=2.0.1

ENV ANDROID_SDK_URL="https://dl.google.com/android/repository/tools_r${ANDROID_SDK_TOOLS_VERSION}-linux.zip" \
    NODEJS_URL="https://nodejs.org/dist/v${NODEJS_VERSION}/node-v${NODEJS_VERSION}-linux-x64.tar.gz" \
    ANDROID_SDK_PACKAGES="platform-tools,android-${ANDROID_TARGET_SDK_VERSION},build-tools-${ANDROID_BUILD_TOOLS_VERSION},extra-android-m2repository,extra-android-support" \
    PATH="$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/$ANDROID_BUILD_TOOLS_VERSION:$NODE_PATH/bin"

# Install basic tools and dependencies
RUN dpkg --add-architecture i386 && \
    apt-get -qq update && \
    apt-get install -y \
      openjdk-8-jdk=${JDK_VERSION} \
      git \
      curl \
      wget \
      unzip \
      libc6:i386 \
      libstdc++6:i386 \
      libgcc1:i386 \
      zlib1g:i386 \
      libncurses5:i386 \
      libz1:i386 && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get clean

# Install Android SDK
RUN mkdir -p ${ANDROID_HOME} && \
    cd ${ANDROID_HOME} && wget -q ${ANDROID_SDK_URL} -O android-sdk-tools.zip && \
    unzip -q ${ANDROID_HOME}/android-sdk-tools.zip -d ${ANDROID_HOME} && \
    cd ${ANDROID_HOME} && rm -f android-sdk-tools.zip && \
    chmod a+x -R $ANDROID_HOME && chown -R root:root $ANDROID_HOME && \
    echo y | android update sdk -a -u -t ${ANDROID_SDK_PACKAGES} && \
    mkdir -p $ANDROID_HOME/licenses/ && \
    echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > $ANDROID_HOME/licenses/android-sdk-license && \
    echo "84831b9409646a918e30573bab4c9c91346d8abd" > $ANDROID_HOME/licenses/android-sdk-preview-license

# Install Node
RUN apt-get -qq update && \
    apt-get install -y ca-certificates --no-install-recommends && \
    mkdir -p ${NODE_PATH} && \
    curl -sL ${NODEJS_URL} | tar xz --strip-components=1 -C ${NODE_PATH} && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Install React Native
RUN npm install -g react-native-cli@${REACT_NATIVE_CLI_VERSION}
