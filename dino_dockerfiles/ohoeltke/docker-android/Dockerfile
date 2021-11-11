FROM beevelop/java

MAINTAINER Maik Hummel <m@ikhummel.com>

ENV ANDROID_SDK_URL="https://dl.google.com/android/repository/tools_r25.2.5-linux.zip" \
    ANDROID_BUILD_TOOLS_VERSION=28.0.3 \
#    ANDROID_APIS="android-10,android-15,android-16,android-17,android-18,android-19,android-20,android-21,android-22,android-23,android-24,android-25" \
    ANDROID_APIS="android-25" \
    ANT_HOME="/usr/share/ant" \
    MAVEN_HOME="/usr/share/maven" \
    GRADLE_URL="https://services.gradle.org/distributions/gradle-3.4.1-bin.zip" \
    GRADLE_HOME="/opt/gradle/gradle-3.4.1" \
    ANDROID_HOME="/opt/android"

ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/$ANDROID_BUILD_TOOLS_VERSION:$ANT_HOME/bin:$MAVEN_HOME/bin:$GRADLE_HOME/bin

WORKDIR /opt

RUN dpkg --add-architecture i386 && \
    apt-get -qq update && \
    apt-get -qq install -y wget curl maven ant git libncurses5:i386 libstdc++6:i386 zlib1g:i386 unzip && \
    
    # Installs Gradle 3.4.1
    wget -O gradle.zip ${GRADLE_URL} && \
    mkdir /opt/gradle && \
    unzip -d /opt/gradle gradle.zip && rm gradle.zip && \
    mkdir /.gradle && \
    chmod a+wx -R /.gradle && \
    # Installs Android SDK
    mkdir android && cd android && \
    wget -O tools.zip ${ANDROID_SDK_URL} && \
    unzip tools.zip && rm tools.zip && \
    echo y | android update sdk -a -u -t platform-tools,${ANDROID_APIS},build-tools-${ANDROID_BUILD_TOOLS_VERSION} && \
    chmod a+wx -R $ANDROID_HOME && \
    chown -R root:root $ANDROID_HOME && \
    # add dir for npm
    mkdir  /.npm && \
    chmod a+wx -R /.npm && \

    # So, we need to add the licenses here while it's still valid.
    # The hashes are sha1s of the licence text, which I imagine will be periodically updated, so this code will 
    # only work for so long.
    mkdir "$ANDROID_HOME/licenses" || true && \
    echo -e "\nd56f5187479451eabf01fb78af6dfcb131a6481e\n8933bad161af4178b1185d1a37fbf41ea5269c55\n24333f8a63b6825ea9c5514f83c2829b004d1fee" > "$ANDROID_HOME/licenses/android-sdk-license" && \
    echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" > "$ANDROID_HOME/licenses/android-sdk-preview-license" && \
    echo -e "\n601085b94cd77f0b54ff86406957099ebe79c4d6" > "$ANDROID_HOME/licenses/android-googletv-license" && \
    echo -e "\n33b6a2b64607f11b759f320ef9dff4ae5c47d97a" > "$ANDROID_HOME/licenses/google-gdk-license" && \
    echo -e "\nd975f751698a77b662f1254ddbeed3901e976f5a" > "$ANDROID_HOME/licenses/intel-android-extra-license" && \
    echo -e "\ne9acab5b5fbb560a72cfaecce8946896ff6aab9d" > "$ANDROID_HOME/licenses/mips-android-sysimage-license" && \
    
    # Clean up
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get autoremove -y && \
    apt-get clean
