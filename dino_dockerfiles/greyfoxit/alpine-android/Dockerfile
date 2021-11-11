FROM greyfoxit/alpine-openjdk8:8u131

# maintainer: Greyfox Team | team@greyfox.it | @greyfoxit

# Setup

ENV VERSION_SDK_TOOLS=3952940 \
	  ANDROID_HOME=/usr/local/android-sdk-linux

ENV	PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools

RUN mkdir -p $ANDROID_HOME && \
    chown -R root.root $ANDROID_HOME && \

# Install dependencies

apk add --no-cache bash curl git openssl openssh-client ca-certificates && \

# Install Android SDK

wget -q -O sdk.zip http://dl.google.com/android/repository/sdk-tools-linux-$VERSION_SDK_TOOLS.zip && \
unzip sdk.zip -d $ANDROID_HOME && \
rm -f sdk.zip

# Install and update Android packages

ADD packages.txt $ANDROID_HOME

RUN mkdir -p /root/.android && \
    touch /root/.android/repositories.cfg && \

sdkmanager --update && yes | sdkmanager --licenses && \
sdkmanager --package_file=$ANDROID_HOME/packages.txt
