FROM ubuntu:xenial

################################################################################################
###
### Install JAVA
###
RUN apt-get update && apt-get -y install openjdk-8-jdk

################################################################################################
###
### Install RUBY
###
RUN apt-get update && apt-get -y install ruby-dev

################################################################################################
###
### Download ANDROID SDK
### Inspired from : - https://github.com/cakuki/docker-alpine-android-sdk
###									- https://hub.docker.com/r/thedrhax/android-sdk/~/dockerfile/
###
ENV SDK_VERSION     25.2.3
ENV ANDROID_HOME    /opt/android-sdk-linux

RUN apt-get -y install curl
RUN mkdir "$ANDROID_HOME" .android \
 && cd "$ANDROID_HOME" \
 && curl -o sdk.zip "https://dl.google.com/android/repository/tools_r${SDK_VERSION}-linux.zip" \
 && unzip sdk.zip \
 && rm sdk.zip \
 # Once we have the license, gradle will be able to download the required build-tools
 && mkdir licenses \
 && echo "8933bad161af4178b1185d1a37fbf41ea5269c55\nd56f5187479451eabf01fb78af6dfcb131a6481e" > ${ANDROID_HOME}/licenses/android-sdk-license \
 && echo "84831b9409646a918e30573bab4c9c91346d8abd" > ${ANDROID_HOME}/licenses/android-sdk-preview-license

################################################################################################
###
### Install GRADLE
###
ENV GRADLE_VERSION  2.13
ENV GRADLE_HOME     /opt/gradle-${GRADLE_VERSION}

RUN curl -SLO https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \
	&& mkdir -p "${GRADLE_HOME}" \
	&& unzip "gradle-${GRADLE_VERSION}-bin.zip" -d "/opt" \
	&& rm -f "gradle-${GRADLE_VERSION}-bin.zip"


ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${GRADLE_HOME}/bin

################################################################################################
###
### Install NODE
###
ENV NODE_VERSION  6	

RUN curl -sL "https://deb.nodesource.com/setup_${NODE_VERSION}.x" | bash -
RUN apt-get -y install nodejs

################################################################################################
###
### Install fastlane
###

# Need g++ and make to build gem native extension (which fastlane is)
RUN apt-get install -y g++ make
RUN gem install fastlane
