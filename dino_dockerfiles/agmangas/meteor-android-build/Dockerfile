FROM ubuntu:16.04

# Android SDK variables

ENV ANDROID_SDK_URL https://dl.google.com/android/repository/tools_r25.2.5-linux.zip
ENV ANDROID_SDK_PATH /android
ENV ANDROID_SDK_FILTER platform-tool,android-25,build-tools-25.0.2

# Keystore variables

ENV KEYSTORE_PATH /keys
ENV KEYSTORE_FILE_NAME keystore
ENV KEYSTORE_STOREPASS passwd
ENV KEYSTORE_KEYPASS passwd
ENV KEYSTORE_ALIAS defaultkey
ENV KEYSTORE_DNAME CN=Meteor Android Build, OU=CTIC, O=CTIC, L=Gijon, ST=Asturias, C=ES
ENV KEYSTORE_KEYALG RSA
ENV KEYSTORE_KEYSIZE 2048
ENV KEYSTORE_VALIDITY 10000

# App variables

ENV APP_PATH /app
ENV APP_BUILD_PATH /build
ENV SCRIPTS_PATH /scripts

# Copy scripts

RUN mkdir -p $SCRIPTS_PATH

WORKDIR $SCRIPTS_PATH

COPY ./install-node-meteor.sh ./
COPY ./tar-override.sh ./
COPY ./tar-restore.sh ./

RUN chmod -R +x .

# Install package dependencies

RUN apt-get update && apt-get install -y openjdk-8-jdk wget curl \
	build-essential chrpath libssl-dev libxft-dev libfreetype6 \
	libfreetype6-dev libfontconfig1 libfontconfig1-dev python git unzip

# Install Meteor and Node

WORKDIR $SCRIPTS_PATH

RUN bash ./install-node-meteor.sh

# Download and extract the Android SDK

RUN mkdir -p $ANDROID_SDK_PATH

WORKDIR $ANDROID_SDK_PATH

RUN wget $ANDROID_SDK_URL -O android-sdk.zip
RUN unzip android-sdk.zip -d android-sdk-linux
RUN rm -fr android-sdk.zip

# Install the Android SDK

WORKDIR $ANDROID_SDK_PATH/android-sdk-linux

RUN echo "y" | tools/android update sdk --no-ui --all --filter $ANDROID_SDK_FILTER

# Update Android SDK environment variables

ENV ANDROID_HOME $ANDROID_SDK_PATH/android-sdk-linux
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

# Create default keystore (user should provide her own)

ENV KEYSTORE_FILE_PATH $KEYSTORE_PATH/$KEYSTORE_FILE_NAME

RUN mkdir -p $KEYSTORE_PATH

RUN keytool -genkey -noprompt -alias $KEYSTORE_ALIAS -dname "$KEYSTORE_DNAME" \
    -keystore $KEYSTORE_FILE_PATH -storepass $KEYSTORE_STOREPASS -keypass $KEYSTORE_KEYPASS \
    -keyalg $KEYSTORE_KEYALG -keysize $KEYSTORE_KEYSIZE -validity $KEYSTORE_VALIDITY

# Initialize the build folder

RUN mkdir -p $APP_BUILD_PATH

VOLUME $APP_BUILD_PATH

# Set build script as default executable

WORKDIR /usr/local/sbin

COPY ./build-android.sh ./
RUN chmod +x ./build-android.sh

CMD ["build-android.sh"]