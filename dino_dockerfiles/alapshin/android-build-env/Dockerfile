FROM openjdk:8

ARG PACKAGES="file git make wget unzip libtinfo5"
ARG ANDROID_SDK_URL="https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip"
ARG ANDROID_PACKAGES="tools platform-tools build-tools;28.0.3 platforms;android-28 extras;google;m2repository extras;android;m2repository"

ENV BUILD_HOME /var/cache/build
# Set environment variables for Android SDK
ENV ANDROID_SDK_ROOT /opt/android-sdk
ENV ANDROID_SDK_HOME /opt/android-sdk
ENV ANDROID_NDK_HOME ${ANDROID_SDK_ROOT}/ndk-bundle

# Install required packages
RUN apt-get update \
    && apt-get install --yes --no-install-recommends --no-install-suggests ${PACKAGES} \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create directory that is used as user home during build
RUN mkdir -p ${BUILD_HOME} \
        && chmod --recursive 777 ${BUILD_HOME}

# Create directory for Android SDK
# Download and install Android SDK and its components
RUN mkdir -p ${ANDROID_SDK_ROOT} \
    && wget --quiet --output-document=${ANDROID_SDK_ROOT}/sdk-tools.zip ${ANDROID_SDK_URL} \
    && unzip -d ${ANDROID_SDK_ROOT} ${ANDROID_SDK_ROOT}/sdk-tools.zip \
    && rm --force ${ANDROID_SDK_ROOT}/sdk-tools.zip \
    # Accept all licenses
    && yes | ${ANDROID_SDK_ROOT}/tools/bin/sdkmanager --licenses \
    # Install sdk packages
    && ${ANDROID_SDK_ROOT}/tools/bin/sdkmanager --verbose ${ANDROID_PACKAGES} \
    # Make directory with sdk writeable for other users
    # This way missing sdk packages could be installed by android gradle plugin
    # during build
    && chmod --recursive 777 ${ANDROID_SDK_ROOT}
