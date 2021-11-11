FROM gradle
LABEL author="Florian baader <florian.baader@selectcode.de>"
LABEL version="1.1"
LABEL description="Container to build android apps"

#Make sure you change these to your needs
ENV ANDROID_TARGET_SDK="27" \
    ANDROID_BUILD_TOOLS="26.0.2"

# Install unzipping tools
RUN sudo apt-get --quiet update --yes
RUN sudo apt-get --quiet install --yes wget tar unzip lib32stdc++6 lib32z1

RUN wget --quiet --output-document=android-sdk.zip https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip && \
    unzip android-sdk.zip -d android-sdk-linux/

# Install the sdks
RUN echo y | android-sdk-linux/tools/bin/sdkmanager "platforms;android-${ANDROID_TARGET_SDK}"
RUN echo y | android-sdk-linux/tools/bin/sdkmanager "tools"
RUN echo y | android-sdk-linux/tools/bin/sdkmanager "build-tools;${ANDROID_BUILD_TOOLS}"

#Install the google play service repo
RUN echo y | android-sdk-linux/tools/bin/sdkmanager "extras;android;m2repository"
RUN echo y | android-sdk-linux/tools/bin/sdkmanager "extras;google;google_play_services"
RUN echo y | android-sdk-linux/tools/bin/sdkmanager "extras;google;m2repository"

# Add the sdk tools to the path variable
RUN export PATH=$PATH:$PWD/android-sdk-linux/platform-tools/

# Set the android home variable
ENV ANDROID_HOME $PWD/android-sdk-linux

