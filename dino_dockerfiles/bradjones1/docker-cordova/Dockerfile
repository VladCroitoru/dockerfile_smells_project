FROM openjdk:8-jdk

# Install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - \
  && apt-get update && apt-get install -yqq apt-transport-https \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
  && echo "deb https://deb.nodesource.com/node_6.x stretch main" | tee /etc/apt/sources.list.d/nodesource.list \
  && apt-get update && apt-get install -yqq yarn \
  && rm -rf /var/lib/apt/lists/*

# download and extract android sdk
RUN curl -L -o temp.zip https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip \
  && unzip -d /usr/local/android-sdk-linux temp.zip && rm temp.zip
ENV ANDROID_HOME /usr/local/android-sdk-linux
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

# download and install gradle.
ENV GRADLE_VERSION 4.2.1
RUN curl -s -L -o temp.zip https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip \
  && unzip -d /usr/local temp.zip && rm temp.zip
ENV PATH $PATH:/usr/local/gradle-$GRADLE_VERSION/bin

ENV ANDROID_SDK_HOME /tmp
RUN mkdir -p /tmp/.android && touch /tmp/.android/repositories.cfg
# update and accept licences
RUN mkdir -p ${ANDROID_HOME}/licenses
RUN echo -en "8933bad161af4178b1185d1a37fbf41ea5269c55\nd56f5187479451eabf01fb78af6dfcb131a6481e" > ${ANDROID_HOME}/licenses/android-sdk-license
# Install some basic dependencies and let Gradle install what it wants.
RUN /usr/local/android-sdk-linux/tools/bin/sdkmanager \
  "platform-tools" \
  "extras;android;m2repository" \
  && chmod -R 777 $ANDROID_HOME \
  && chmod -R 777 /tmp/.android

ENV GRADLE_USER_HOME /src/gradle

VOLUME /src
WORKDIR /src
