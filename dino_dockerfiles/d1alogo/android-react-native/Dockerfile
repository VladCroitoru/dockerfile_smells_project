FROM openjdk:8-jdk
MAINTAINER Pin <pinfake@hotmail.com>


ENV ANDROID_HOME="/opt/android-sdk-linux"
ENV LD_LIBRARY_PATH="${ANDROID_HOME}/tools/lib"
ENV ANDROID_SDK_HOME="${ANDROID_HOME}"
ENV PATH="${ANDROID_HOME}/emulator:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools:${PATH}"
ENV LD_LIBRARY_PATH="${ANDROID_HOME}/tools/lib:${ANDROID_HOME}/emulator/lib64:${ANDROID_HOME}/emulator/lib64/qt/lib:${ANDROID_HOME}/emulator/lib/libstdc++"
ENV TERM=xterm


RUN dpkg --add-architecture i386 && \
    curl -sL https://deb.nodesource.com/setup_4.x | bash - && \
    apt-get install -y nodejs libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 build-essential \
    python-dev autoconf dtach vim tmux libc6:i386 libstdc++6:i386 zlib1g:i386 libgl1-mesa-dri && \
    apt-get clean
RUN npm install -g react-native-cli
RUN cd /tmp && git clone https://github.com/facebook/watchman.git && cd watchman && \
    git checkout v4.1.0 && ./autogen.sh && ./configure && make && make install && rm -rf /tmp/watchman
RUN mkdir /root/.gradle && touch /root/.gradle/gradle.properties && echo "org.gradle.daemon=true" >> /root/.gradle/gradle.properties

RUN cd /tmp && \
    curl -O https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip && \
    cd /opt && mkdir android-sdk-linux && cd android-sdk-linux  && unzip /tmp/*.zip && rm /tmp/*.zip 

RUN echo "y" | sdkmanager "tools"
RUN echo "y" | sdkmanager "sources;android-23"
RUN echo "y" | sdkmanager "platforms;android-23"
RUN echo "y" | sdkmanager "sources;android-24"
RUN echo "y" | sdkmanager "platforms;android-24"
RUN echo "y" | sdkmanager "sources;android-25"
RUN echo "y" | sdkmanager "platforms;android-25"
RUN echo "y" | sdkmanager "sources;android-26"
RUN echo "y" | sdkmanager "platforms;android-26"
RUN echo "y" | sdkmanager "sources;android-27"
RUN echo "y" | sdkmanager "platforms;android-27"
RUN echo "y" | sdkmanager "build-tools;23.0.1"
RUN echo "y" | sdkmanager "build-tools;24.0.3"
RUN echo "y" | sdkmanager "build-tools;25.0.3"
RUN echo "y" | sdkmanager "build-tools;26.0.2"
RUN echo "y" | sdkmanager "build-tools;27.0.3"
RUN echo "y" | sdkmanager "extras;android;m2repository"
RUN echo "y" | sdkmanager "extras;google;m2repository"

#
#RUN echo "y" | android update sdk --no-ui --force -a --filter extra-android-m2repository,extra-android-support,extra-google-m2repository,platform-tools,android-23,build-tools-23.0.1


RUN echo "export PATH=${PATH}" > /root/.profile
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
