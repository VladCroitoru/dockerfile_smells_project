# Pull base image.
FROM openjdk:8-jdk
# original maintainer: navarroaxel <navarroaxel@gmail.com>
MAINTAINER hafiyyan94 <hafiyyan94@gmail.com>

# Install base software packagages
ENV ANDROID_COMPILE_SDK "25"
ENV ANDROID_BUILD_TOOLS "25.0.3"
ENV ANDROID_SDK_TOOLS "3859397"  # "26.0.1"
ENV ANDROID_CMAKE_REV "3.6.3155560"
ENV GIT_SUBMODULE_STRATEGY recursive # Remove if you don't have to clone submodules
#Installing Dependencies
RUN mkdir $HOME/.android # For sdkmanager configs
RUN echo 'count=0' > $HOME/.android/repositories.cfg # Avoid warning
RUN wget --output-document=android-sdk.zip https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
RUN mkdir /android-sdk-linux
RUN unzip -qq android-sdk.zip -d /android-sdk-linux
ENV ANDROID_HOME=/android-sdk-linux
RUN export PATH=$PATH:$ANDROID_HOME/platform-tools/:$ANDROID_NDK_HOME
RUN echo y | $ANDROID_HOME/tools/bin/sdkmanager --update 
RUN echo y | $ANDROID_HOME/tools/bin/sdkmanager 'tools'
RUN echo y | $ANDROID_HOME/tools/bin/sdkmanager 'platform-tools'
RUN echo y | $ANDROID_HOME/tools/bin/sdkmanager 'build-tools;'$ANDROID_BUILD_TOOLS
RUN echo y | $ANDROID_HOME/tools/bin/sdkmanager 'platforms;android-'$ANDROID_COMPILE_SDK
RUN echo y | $ANDROID_HOME/tools/bin/sdkmanager 'extras;android;m2repository'
RUN echo y | $ANDROID_HOME/tools/bin/sdkmanager 'extras;google;google_play_services'
RUN echo y | $ANDROID_HOME/tools/bin/sdkmanager 'extras;google;m2repository'
RUN echo y | $ANDROID_HOME/tools/bin/sdkmanager 'cmake;'$ANDROID_CMAKE_REV
