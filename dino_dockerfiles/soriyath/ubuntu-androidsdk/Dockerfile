FROM soriyath/ubuntu-swissfr:xenial
MAINTAINER Sumi Straessle

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -o Dpkg::Options::="--force-overwrite" install -y openjdk-9-jdk	
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y android-sdk \
	adb \
	android-sdk-common \
	android-sdk-build-tools \
	android-sdk-build-tools-common \
	android-sdk-platform-tools \
	android-sdk-platform-tools-common

# Clean
RUN DEBIAN_FRONTEND=noninteractive apt-get clean \
	&& apt-get autoremove \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV ANDROID_HOME=/usr/lib/android-sdk
ENV PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools