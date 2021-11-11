FROM openjdk:8-jdk

RUN dpkg --add-architecture i386 && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y expect \
    curl \
    maven \
    ant \
    gradle \
    libncurses5:i386 \
    libstdc++6:i386 \
    zlib1g:i386

ENV ANDROID_SDK_URL="https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip" \
    ANDROID_BUILD_TOOLS_VERSION=26.0.1 \
    ANDROID_APIS="android-19,android-20,android-21,android-22,android-23,android-24,android-25,android-26" \
    ANT_HOME="/usr/share/ant" \
    MAVEN_HOME="/usr/share/maven" \
    GRADLE_HOME="/usr/share/gradle" \
    ANDROID_HOME="/opt/android"

ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/$ANDROID_BUILD_TOOLS_VERSION:$ANT_HOME/bin:$MAVEN_HOME/bin:$GRADLE_HOME/bin

WORKDIR /opt

# Installs Android SDK
RUN mkdir android && cd android && \
    wget -O tools.zip ${ANDROID_SDK_URL} && \
    unzip tools.zip && rm tools.zip && \
    echo y | android update sdk -a -u -t "platform-tools,${ANDROID_APIS},build-tools;${ANDROID_BUILD_TOOLS_VERSION}" && \
    chmod a+x -R $ANDROID_HOME && \
    chown -R root:root $ANDROID_HOME && \

    # Clean up
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get autoremove -y && \
    apt-get clean

COPY ./accept-licenses.sh ./accept-licenses.sh

RUN ./accept-licenses.sh && rm ./accept-licenses.sh

