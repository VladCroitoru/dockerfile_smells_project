# Inspired by:
# https://github.com/jangrewe/gitlab-ci-android/blob/master/Dockerfile
# https://github.com/51systems/gitlab-ci-android/blob/master/Dockerfile
# https://github.com/reddit/docker-android-build/blob/master/Dockerfile

FROM ubuntu:16.04
MAINTAINER Iain Connor <i.connor@tippingcanoe.com>

ENV DEBIAN_FRONTEND noninteractive

ENV VERSION_SDK_TOOLS "25.1.7"
ENV VERSION_BUILD_TOOLS "24.0.2"
ENV VERSION_TARGET_SDK "24"
ENV VERSION_EMULATOR_GOOGLE_APIS_TARGET_SDK "23"
# There's no 24 emulator with Google APIs yet.

ENV ANDROID_HOME "/sdk"
ENV PATH "$PATH:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools"

# Install dependencies

RUN apt-get -qq update && \
    apt-get install -qqy --no-install-recommends \
        curl \
        html2text \
        openjdk-8-jdk \
        libc6-i386 \
        lib32stdc++6 \
        lib32gcc1 \
        lib32ncurses5 \
        lib32z1 \
        unzip \
        wget \
        build-essential \
        expect \
        file \
        libmagic1 \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Fix certificates

RUN rm -f /etc/ssl/certs/java/cacerts; \
    /var/lib/dpkg/info/ca-certificates-java.postinst configure

# Install the SDK tools

ADD http://dl.google.com/android/repository/tools_r${VERSION_SDK_TOOLS}-linux.zip /tools.zip
RUN unzip /tools.zip -d /${ANDROID_HOME} && \
    rm -v /tools.zip

# Install our helpers

COPY tools /usr/local/bin/tools
RUN chmod +x /usr/local/bin/tools/agree-to-licenses.sh
RUN chmod +x /usr/local/bin/tools/wait-for-emulator.sh

# And use them to install Android dependencies

RUN /usr/local/bin/tools/agree-to-licenses.sh \
  "android update sdk --all --no-ui --filter platform-tools,android-${VERSION_TARGET_SDK},android-${VERSION_EMULATOR_GOOGLE_APIS_TARGET_SDK},build-tools-${VERSION_BUILD_TOOLS},sys-img-armeabi-v7a-android-${VERSION_TARGET_SDK},sys-img-armeabi-v7a-google_apis-${VERSION_EMULATOR_GOOGLE_APIS_TARGET_SDK},extra-android-support,extra-android-m2repository,extra-google-m2repository,extra-google-google_play_services"

# Create emulators

RUN android list targets

# Without Google APIs
RUN echo "no" | android create avd \
                --force \
                --device "Nexus 5" \
                --name nexus5_${VERSION_TARGET_SDK} \
                --target android-${VERSION_TARGET_SDK} \
                --abi default/armeabi-v7a \
                --skin WVGA800 \
                --sdcard 512M

# With Google APIs
RUN echo "no" | android create avd \
                --force \
                --device "Nexus 5" \
                --name nexus5_${VERSION_EMULATOR_GOOGLE_APIS_TARGET_SDK} \
                --target android-${VERSION_EMULATOR_GOOGLE_APIS_TARGET_SDK} \
                --abi google_apis/armeabi-v7a \
                --skin WVGA800 \
                --sdcard 512M

# Boot up the emulators

# Without Google APIs
RUN /bin/bash -c "SHELL=/bin/bash emulator -avd nexus5_${VERSION_TARGET_SDK} -no-skin -no-audio -no-window & \
    adb wait-for-device && \
    /usr/local/bin/tools/wait-for-emulator.sh" && \
    adb -s emulator-5554 emu kill


# With Google APIs
RUN /bin/bash -c "SHELL=/bin/bash emulator -avd nexus5_${VERSION_EMULATOR_GOOGLE_APIS_TARGET_SDK} -no-skin -no-audio -no-window & \
    adb wait-for-device && \
    /usr/local/bin/tools/wait-for-emulator.sh" && \
    adb -s emulator-5554 emu kill
