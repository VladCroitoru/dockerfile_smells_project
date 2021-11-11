FROM openjdk:8-jdk

# Set bash as entrypoint
CMD ["/bin/bash"] 

# Dependencies
RUN apt-get update && apt-get install -y \
    apt-utils \
    file \
    git \
    lib32stdc++6 \ 
    lib32z1 \
    sudo \
    tar \
    unzip \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Add user and move to its home
RUN useradd -m -s /bin/bash build && \
    echo "build ALL=NOPASSWD: ALL" > /etc/sudoers.d/build
USER build
WORKDIR /home/build

# Set env
ENV HOME="/home/build"
ENV ANDROID_HOME="$HOME/android-sdk-linux" \
    PATH="$PATH:${ANDROID_HOME}/platform-tools/:${HOME}/bin/"

# Download android-wait-for-emulator
RUN wget --quiet --output-document=android-wait-for-emulator "https://raw.githubusercontent.com/travis-ci/travis-cookbooks/0f497eb71291b52a703143c5cd63a217c8766dc9/community-cookbooks/android-sdk/files/default/android-wait-for-emulator" && \
    chmod a+x android-wait-for-emulator && \
    mkdir -p bin && \
    mv android-wait-for-emulator bin/

# Variables for easier updating
ENV COMPILE_SDK="26" \
    TEST_SDK="25" \
    BUILD_TOOLS="25.0.3" \
    TOOLS_URL="https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip"

# Download and unzip SDK tools
RUN wget --output-document=android-sdk.zip "${TOOLS_URL}" && \
    unzip android-sdk.zip -d android-sdk-linux && \
    rm android-sdk.zip

# Install needed SDK components
RUN echo y | android-sdk-linux/tools/bin/sdkmanager --verbose \
    "build-tools;${BUILD_TOOLS}" \
    "emulator" \
    "extras;android;m2repository" \
    "extras;google;google_play_services" \
    "extras;google;m2repository" \
    "platform-tools" \
    "platforms;android-${COMPILE_SDK}" \
    "system-images;android-${TEST_SDK};google_apis;x86_64"

# Create AVD
RUN echo no | android-sdk-linux/tools/bin/avdmanager create avd --force --name test --abi google_apis/x86_64 --package "system-images;android-${TEST_SDK};google_apis;x86_64"

