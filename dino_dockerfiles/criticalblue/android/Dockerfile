
FROM ubuntu:18.04

# == Install required tools
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq && apt-get install -qq -y \
  bc \
  binutils-arm-linux-gnueabi \
  binutils-aarch64-linux-gnu \
  binutils-multiarch \
  curl \
  expect \
  git \
  maven \
  nano \
  python \
  python-dev \
  python-pip \
  python3-pip \
  scons \
  unzip \
  wget \
  zip \
  clang \
  libcapstone3 \
  openjdk-8-jdk-headless \
  tzdata

RUN ln -fs /usr/share/zoneinfo/Europe/London /etc/localtime

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# FIXME: Python stuff should be in a venv handled by .jenkins.sh
ENV PYTHON_REQS "requests PyJWT validators durations pyaxmlparser javalang capstone virtualenv PyInstaller==3.3.1 pure-python-adb boto3 clang==6.0.0"
#RUN pip install  -q $PYTHON_REQS
RUN pip3 install -q $PYTHON_REQS

# Symlink python clang searches for libclang.so only
RUN ln -s /usr/lib/llvm-6.0/lib/libclang.so.1 /usr/lib/llvm-6.0/lib/libclang.so

#Android stuff
RUN apt-get install -qq -y gradle


# 32-bit libraries
RUN dpkg --add-architecture i386 \
 && apt-get update -qq \
 && apt-get install -qq -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 libbz2-1.0:i386

# == Set up Android NDK-related environment
ENV ANDROID_NDK_HOME /opt/android-ndk-r21d
ENV PATH ${PATH}:${ANDROID_NDK_HOME}

# == Download Android NDK and install in /opt/android-ndk-r19
ENV ANDROID_NDK_PACKAGE=android-ndk-r21d-linux-x86_64.zip
RUN cd /opt \
 && wget -q https://dl.google.com/android/repository/${ANDROID_NDK_PACKAGE} \
 && unzip -q ${ANDROID_NDK_PACKAGE} \
 && rm ${ANDROID_NDK_PACKAGE} \
 && test -d "${ANDROID_NDK_HOME}"


# === Install Android SDKs
ENV ANDROID_HOME /opt/android-sdk-linux
ENV ANDROID_SDK_FILENAME sdk-tools-linux-4333796.zip
ENV ANDROID_SDK_URL https://dl.google.com/android/repository/${ANDROID_SDK_FILENAME}
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin

RUN cd /opt && \
    wget -q ${ANDROID_SDK_URL} && \
    unzip -q ${ANDROID_SDK_FILENAME} && \
    rm ${ANDROID_SDK_FILENAME} && \
    mkdir ${ANDROID_HOME} && \
    mv tools ${ANDROID_HOME}

# Create home directory and make it writable so jenkins can invoke gradle safely
RUN mkdir $ANDROID_HOME/.android && \
	chmod 777 $ANDROID_HOME/.android

# Accept licenses before installing components, no need to echo y for each component
# License is valid for all the standard components in versions installed from this file
# Non-standard components: MIPS system images, preview versions, GDK (Google Glass) and Android Google TV require separate licenses, not accepted there
RUN yes | sdkmanager --licenses

# Platform tools
RUN sdkmanager "emulator" "tools" "platform-tools"

# SDKs
# Please keep these in descending order!
# The `yes` is for accepting all non-standard tool licenses.
RUN mkdir -p /root/.android/ && touch /root/.android/repositories.cfg
RUN sdkmanager --update
# Please keep all sections in descending order!
RUN yes | sdkmanager \
    "platforms;android-30" \
    "platforms;android-29" \
    "platforms;android-28" \
    "platforms;android-27" \
    "platforms;android-26" \
    "platforms;android-25" \
    "build-tools;30.0.2" \
    "build-tools;30.0.1" \
    "build-tools;30.0.0" \
    "build-tools;29.0.3" \
    "build-tools;29.0.2" \
    "build-tools;29.0.1" \
    "build-tools;29.0.0" \
    "build-tools;28.0.3" \
    "build-tools;28.0.2" \
    "build-tools;28.0.1" \
    "build-tools;28.0.0" \
    "build-tools;27.0.3" \
    "build-tools;27.0.2" \
    "build-tools;27.0.1" \
    "build-tools;27.0.0" \
    "build-tools;26.0.2" \
    "build-tools;26.0.1" \
    "build-tools;25.0.3" \
    "system-images;android-28;google_apis_playstore;x86" \
    "extras;android;m2repository" \
    "extras;google;m2repository" \
    "extras;google;google_play_services" \
    "extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2" \
    "extras;m2repository;com;android;support;constraint;constraint-layout;1.0.1" 


# --- Install Gradle from PPA

# Gradle PPA
RUN apt-get update \
 && apt-get -y install gradle \
 && gradle -v

# ------------------------------------------------------

# jd-cmd
RUN cd /opt && \
 curl -L https://github.com/kwart/jd-cmd/releases/download/jd-cmd-0.9.2.Final/jd-cli-0.9.2-dist.zip > jd-cmd.zip && \
 unzip jd-cmd.zip && \
 cp jd-cli jd-cli.jar /usr/local/bin && \
 rm -fr jd-cmd.zip

RUN echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" >> "$ANDROID_HOME/licenses/android-sdk-license" && \
    echo -e "\n24333f8a63b6825ea9c5514f83c2829b004d1fee" >> "$ANDROID_HOME/licenses/android-sdk-license"
