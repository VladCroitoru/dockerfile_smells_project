FROM openjdk

# Install node
ENV NVM_DIR /root/.nvm
ENV NODE_VERSION 9.1.0

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.6/install.sh | bash
RUN . ${NVM_DIR}/nvm.sh && \
  nvm install ${NODE_VERSION} && \
  nvm alias default $NODE_VERSION && \
  nvm use default

ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH


# Install cordova
RUN npm install -g cordova


# Install gradle and i386 architecture (required for running 32 bit Android tools)
RUN dpkg --add-architecture i386 && \
    rm -rf /var/lib/apt/lists/* && apt-get clean && apt-get update -y && \
    apt-get install -y gradle libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoremove -y && \
    apt-get clean


# Install Android SDK
ENV ANDROID_SDK_FILENAME sdk-tools-linux-3859397.zip
ENV ANDROID_SDK_URL https://dl.google.com/android/repository/${ANDROID_SDK_FILENAME}
ENV ANDROID_HOME /opt/android-sdk
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools
RUN cd /opt && \
    wget -q ${ANDROID_SDK_URL} && \
    unzip ${ANDROID_SDK_FILENAME} -d android-sdk && \
    rm ${ANDROID_SDK_FILENAME}

# Accept license
RUN mkdir -p ${ANDROID_HOME}/licenses && \
  echo 8933bad161af4178b1185d1a37fbf41ea5269c55 > ${ANDROID_HOME}/licenses/android-sdk-license


# Install packages
RUN mkdir /root/.android && touch /root/.android/repositories.cfg
RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses 
RUN ${ANDROID_HOME}/tools/bin/sdkmanager \
  tools \
  platform-tools \
  "platforms;android-25" \
  "platforms;android-26" \
  "build-tools;26.0.2" \
  "extras;android;m2repository"
