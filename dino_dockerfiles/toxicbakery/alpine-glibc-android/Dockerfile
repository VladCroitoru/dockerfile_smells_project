FROM frolvlad/alpine-glibc:alpine-3.8_glibc-2.28

ARG ANDROID_TARGET_SDK=28
ARG ANDROID_BUILD_TOOLS=28.0.3
ARG ANDROID_SDK_TOOLS=4333796
ARG SONAR_CLI=3.3.0.1492

ENV ANDROID_HOME=${PWD}/android-sdk-linux
ENV PATH=${PATH}:${ANDROID_HOME}/platform-tools
ENV PATH=${PATH}:${ANDROID_HOME}/tools
ENV PATH=${PATH}:${ANDROID_HOME}/tools/bin
ENV PATH=${PATH}:${ANDROID_NDK}
ENV PATH=${PATH}:/root/gcloud/google-cloud-sdk/bin
ENV PATH=${PATH}:/root/sonar/bin

RUN apk --no-cache add bash wget gnupg openjdk8 unzip git curl python3 bzip2 \
 && pip3 install --upgrade pip setuptools \
 && update-ca-certificates \
 && pip install -U setuptools \
 && pip install -U wheel \
 && pip install -U crcmod \
# gcloud
 && curl -sSL https://sdk.cloud.google.com > /tmp/gcl && bash /tmp/gcl --install-dir=/root/gcloud --disable-prompts \
 && rm -rf /tmp/gcl \
# Sonar
 && wget -q -O sonar.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_CLI}-linux.zip \
 && unzip -qo sonar.zip \
 && mv sonar-scanner-${SONAR_CLI}-linux /root/sonar \
# SDK
 && wget -q -O android-sdk.zip https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_TOOLS}.zip \
 && mkdir ${ANDROID_HOME} \
 && unzip -qo android-sdk.zip -d ${ANDROID_HOME} \
 && chmod +x ${ANDROID_HOME}/tools/android \
 && rm android-sdk.zip \
# Config
 && mkdir -p ~/.gradle \
 && echo "org.gradle.daemon=false" >> ~/.gradle/gradle.properties \
 && mkdir ~/.android \
 && touch ~/.android/repositories.cfg \
 && yes | sdkmanager --licenses > /dev/null \
 && sdkmanager --update > /dev/null \
 && sdkmanager "platforms;android-${ANDROID_TARGET_SDK}" "build-tools;${ANDROID_BUILD_TOOLS}" platform-tools tools > /dev/null
