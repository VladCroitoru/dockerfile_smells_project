FROM openjdk:8

# Install Git and dependencies
RUN dpkg --add-architecture i386 \
 && apt-get update \
 && apt-get install -y file git curl zip libncurses5:i386 libstdc++6:i386 zlib1g:i386 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists /var/cache/apt

# Set up environment variables
ENV ANDROID_HOME="/home/user/android-sdk-linux" \
    SDK_URL="https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip" \
    GRADLE_URL="https://services.gradle.org/distributions/gradle-4.6-all.zip"

# Create a non-root user
RUN useradd -m user
USER user
WORKDIR /home/user

# Download Android SDK
RUN mkdir "$ANDROID_HOME" .android \
 && cd "$ANDROID_HOME" \
 && curl -o sdk.zip $SDK_URL \
 && unzip sdk.zip \
 && rm sdk.zip 
 
# Create repositories.cfg
RUN touch .android/repositories.cfg
 
# Accept all licences 
RUN ./android-sdk-linux/tools/bin/sdkmanager "build-tools;26.0.2" "platforms;android-26"
RUN yes | ./android-sdk-linux/tools/bin/sdkmanager --update
RUN yes | ./android-sdk-linux/tools/bin/sdkmanager --licenses

 
# Install Gradle
RUN wget $GRADLE_URL -O gradle.zip \
 && unzip gradle.zip \
 && mv gradle-4.6 gradle \
 && rm gradle.zip \
 && mkdir .gradle

ENV PATH="/home/user/gradle/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${PATH}"
