FROM ubuntu:17.10

ENV SDK_TOOLS "3859397"
ENV BUILD_TOOLS "26.0.2"
ENV TARGET_SDK "26"
ENV ANDROID_HOME "/sdk"
ENV PATH "${PATH}:${ANDROID_HOME}/tools"
ENV GRADLE_HOME /gradle
ENV GRADLE_VERSION 4.6
ENV DEBIAN_FRONTEND noninteractive

ARG GRADLE_DOWNLOAD_SHA256=98bd5fd2b30e070517e03c51cbb32beee3e2ee1a84003a5a5d748996d4b1b915

RUN dpkg --add-architecture i386

RUN apt-get update && apt-get install -qqy --no-install-recommends \
    bash \
    bzip2 \
    html2text \
    libc6-i386 \
    lib32stdc++6 \
    lib32gcc1 \
    lib32ncurses5 \
    lib32z1 \
    zlib1g-dev \
    qtbase5-dev \
    qtdeclarative5-dev \
    openjdk-8-jdk \
    qemu-kvm \
    unzip \
    wget \
    python2.7 \
    build-essential \
    python2.7-dev \
    yamdi \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    
RUN echo "Downloading Gradle" \
	&& wget --no-verbose --output-document=gradle.zip "https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" \
	&& echo "Checking download hash" \
	&& echo "${GRADLE_DOWNLOAD_SHA256} *gradle.zip" | sha256sum -c \
	&& echo "Installing Gradle" \
	&& unzip gradle.zip \
	&& rm gradle.zip \
	&& mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" \
	&& ln -s "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle

# Install video tool
RUN wget -nv https://pypi.python.org/packages/1e/8e/40c71faa24e19dab555eeb25d6c07efbc503e98b0344f0b4c3131f59947f/vnc2flv-20100207.tar.gz && tar -zxvf vnc2flv-20100207.tar.gz && rm vnc2flv-20100207.tar.gz && \
    cd vnc2flv-20100207 && ln -s /usr/bin/python2.7 /usr/bin/python && python setup.py install

# Download and extract Android Tools
RUN wget http://dl.google.com/android/repository/sdk-tools-linux-${SDK_TOOLS}.zip -O /tmp/tools.zip && \
    mkdir -p ${ANDROID_HOME} && \
    unzip /tmp/tools.zip -d ${ANDROID_HOME} && \
    rm -v /tmp/tools.zip && \
    ln -s "${ANDROID_HOME}/tools/bin/sdkmanager" /usr/bin/sdkmanager && \
    ln -s "${ANDROID_HOME}/tools/bin/avdmanager" /usr/bin/avdmanager && \
    ln -s "${ANDROID_HOME}/tools/emulator" /usr/bin/emulator

# Install SDK Packages
RUN mkdir -p "${ANDROID_HOME}/licenses/" && \
    printf "8933bad161af4178b1185d1a37fbf41ea5269c55\\nd56f5187479451eabf01fb78af6dfcb131a6481e" > "${ANDROID_HOME}/licenses/android-sdk-license" && \
    printf "84831b9409646a918e30573bab4c9c91346d8abd\\n504667f4c0de7af1a06de9f4b1727b84351f2910" > "${ANDROID_HOME}/licenses/android-sdk-preview-license"

RUN mkdir -p /root/.android/ && touch /root/.android/repositories.cfg && \
    sdkmanager --update    
    
RUN yes | sdkmanager "--licenses"

ADD packages.txt /sdk

RUN while read -r package; do PACKAGES="${PACKAGES}${package} "; done < /sdk/packages.txt && \
    "${ANDROID_HOME}/tools/bin/sdkmanager" ${PACKAGES}
    
RUN mkdir /sdk/tools/keymaps && \
    touch /sdk/tools/keymaps/en-us

RUN mkdir /helpers

COPY wait-for-avd-boot.sh /helpers

VOLUME ["/sdk", "/helpers"]

CMD sdkmanager --update
