FROM quay.io/bitriseio/bitrise-base:alpha

ENV ANDROID_HOME /opt/android-sdk-linux

RUN apt-get update -qq

RUN dpkg --add-architecture i386
RUN apt-get update -qq
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-8-jdk libc6:i386 libstdc++6:i386 libgcc1:i386 libncurses5:i386 libz1:i386


RUN cd /opt \
    && wget -q https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip -O android-sdk-tools.zip \
    && unzip -q android-sdk-tools.zip -d ${ANDROID_HOME} \
    && rm android-sdk-tools.zip

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools
RUN yes | sdkmanager --licenses

# Platform tools
RUN sdkmanager "emulator" "tools" "platform-tools"

# Please keep all sections in descending order!
RUN yes | sdkmanager "system-images;android-26;google_apis;x86"

RUN avdmanager create avd -n pixel2 -d "pixel_xl" -k "system-images;android-26;google_apis;x86"
