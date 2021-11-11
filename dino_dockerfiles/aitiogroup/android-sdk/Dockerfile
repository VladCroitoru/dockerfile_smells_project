FROM openjdk:8-jdk

# Download and install Android SDK
ENV ANDROID_SDK_DOWNLOAD_URL https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip

RUN cd /usr/local/ \
	&& curl -L $ANDROID_SDK_DOWNLOAD_URL -o android-sdk-linux.zip \
	&& unzip android-sdk-linux.zip -d android-sdk-linux \
	&& rm -f android-sdk-linux.zip

# Set environment variables and add to PATH
ENV ANDROID_HOME /usr/local/android-sdk-linux
ENV PATH $PATH:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools

# Install Android SDK packages
RUN yes | $ANDROID_HOME/tools/bin/sdkmanager "build-tools;26.0.1" 
RUN yes | $ANDROID_HOME/tools/bin/sdkmanager "platforms;android-26"

# <<< add custom packages here >>>

# Accept Android SDK licenses
RUN yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses

