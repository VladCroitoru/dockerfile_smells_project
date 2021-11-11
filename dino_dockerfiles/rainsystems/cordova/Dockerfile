FROM java:8-jdk

ENV ANDROID_SDK_URL="https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz" \
    ANDROID_BUILD_TOOLS_VERSION=23.0.3 \
    ANDROID_APIS="android-10,android-15,android-16,android-17,android-18,android-19,android-20,android-21,android-22,android-23" \
    ANT_HOME="/usr/share/ant" \
    MAVEN_HOME="/usr/share/maven" \
    GRADLE_HOME="/usr/share/gradle" \
    ANDROID_HOME="/opt/android-sdk-linux" \
    NODEJS_VERSION=6.2.2 \
    PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/$ANDROID_BUILD_TOOLS_VERSION:$ANT_HOME/bin:$MAVEN_HOME/bin:$GRADLE_HOME/bin:/opt/node/bin \
    CORDOVA_VERSION=6.2.0

RUN dpkg --add-architecture i386 && \
    apt-get -qq update && \
    apt-get -qq install -y \
    ant \
    build-essential \
    ca-certificates \
    curl \
    git \
    gradle \
    libncurses5:i386 \
    libstdc++6:i386 \
    zlib1g:i386 \
    --no-install-recommends \
    && \
    # Installs Android SDK
    curl -sL ${ANDROID_SDK_URL} | tar xz -C /opt && \
    ls -lah /opt/and* && \
    echo $PATH && \
    echo y | /opt/android-sdk-linux/tools/android update sdk -a -u -t platform-tools,${ANDROID_APIS},build-tools-${ANDROID_BUILD_TOOLS_VERSION} && \
    chmod a+x -R $ANDROID_HOME && \
    chown -R root:root $ANDROID_HOME  && \

    # Node
    mkdir -p /opt/node && cd /opt/node && \
    curl -sL https://nodejs.org/dist/v${NODEJS_VERSION}/node-v${NODEJS_VERSION}-linux-x64.tar.gz | tar xz --strip-components=1  && \

    # Cordova
    npm i -g --unsafe-perm cordova@${CORDOVA_VERSION} && \

    # Clean up
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR "/app"

COPY cordova_wrapper.sh /cordova_wrapper.sh
RUN chmod +x /cordova_wrapper.sh

COPY addme.c /
RUN gcc /addme.c -o /addme && chmod 6711 /addme

ENTRYPOINT ["/cordova_wrapper.sh"]
