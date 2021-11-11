#
# Appcelerator Titanium Mobile Build Dockerfile
#
# https://github.com/HazemKhaled/Titanium-Docker
#
# Original repo https://github.com/MartinDevillers/ti.build
#

FROM ubuntu:16.04
MAINTAINER Hazem Khaled <hazem.khaled@gmail.com>

# Install Oracle Java JDK 6
RUN apt-get update
RUN apt-get install -y wget
RUN cd /opt && \
	# Donwloading from Oracel.com needs login, so we use alternative url
	wget http://app.nidc.kr/java/jdk-6u45-linux-x64.bin && \
	chmod +x jdk-6u45-linux-x64.bin && \
	./jdk-6u45-linux-x64.bin

# Set Java Home to JDK6
ENV JAVA_HOME /opt/jdk1.6.0_45/bin/
ENV PATH /opt/jdk1.6.0_45/bin/:${PATH}

# Install necesary packages (i386 stuff is required for Android 32-bit build; gperf is used by ndk-build)
RUN \
	dpkg --add-architecture i386 && \
	apt-get update && \
	apt-get -y install \
	libc6:i386 libncurses5:i386 libstdc++6:i386 zlib1g:i386 \
	unzip \
	gperf

# Grab Android SDK
RUN cd /opt && \
	wget -nv -O android-sdk.tgz http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && \
	tar -xvzf android-sdk.tgz && \
	rm -f android-sdk.tgz

# Install Android SDK 23 and additional tools
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --all --filter android-23,platform-tools,build-tools-21.0.0 --no-ui --force

# Grab Android NDK
RUN cd /opt && \
	wget -nv -O android-ndk.zip https://dl.google.com/android/repository/android-ndk-r12-linux-x86_64.zip && \
	unzip android-ndk.zip && \
	rm -f android-ndk.zip

# Set Android SDK/NDK Environment Variable
ENV ANDROID_SDK /opt/android-sdk-linux
ENV ANDROID_NDK /opt/android-ndk-r10e

# Install nodejs 4.6.x
RUN apt-get install -y python-software-properties
RUN wget https://deb.nodesource.com/setup_4.x
RUN chmod +x setup_4.x && ./setup_4.x
RUN apt-get install -y nodejs

# Install Titanium SDK and Alloy
RUN npm install -g titanium@5.0.14 alloy@1.9.11 tisdk

# Grab Titanium SDK
RUN apt-get install -y libxml2-utils
RUN tisdk install $(echo "cat //sdk-version" | xmllint --shell tiapp.xml | sed '/^\/ >/d' | sed 's/<[^>]*.//g' | echo 6.1.1.GA)

# Configure Android SDK/NDK path in Titanium CLI
RUN titanium config android.sdk /opt/android-sdk-linux
RUN titanium config android.ndk /opt/android-ndk-r10e
