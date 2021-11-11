FROM openjdk:8u222-jdk-stretch

LABEL maintainer "Cedric Gatay <c.gatay@code-troopers.com>"

ARG ANDROID_SDK_TOOLS="4333796"
ARG ANDROID_COMPILE_SDK="28"
ARG ANDROID_BUILD_TOOLS="28.0.2"

RUN apt-get --quiet update --yes \
    && apt upgrade -y \
    && apt-get --quiet install --yes wget tar unzip lib32stdc++6 lib32z1 imagemagick make g++ less \
    && wget --quiet --output-document=android-sdk.zip https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_TOOLS}.zip \
    && unzip -d android-sdk-linux android-sdk.zip \
    && rm -f android-sdk.zip \
    && echo y | android-sdk-linux/tools/bin/sdkmanager "platforms;android-${ANDROID_COMPILE_SDK}" >/dev/null \
    && echo y | android-sdk-linux/tools/bin/sdkmanager "platform-tools" >/dev/null \
    && echo y | android-sdk-linux/tools/bin/sdkmanager "build-tools;${ANDROID_BUILD_TOOLS}" >/dev/null \
    && export ANDROID_HOME=$PWD/android-sdk-linux \
    && export PATH=$PATH:$PWD/android-sdk-linux/platform-tools/ \
    && yes | android-sdk-linux/tools/bin/sdkmanager --licenses \
    && rm -rf /var/lib/apt/lists/*


#RUN gpg --keyserver hkp://pool.sks-keyservers.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
RUN curl -sSL https://rvm.io/mpapis.asc | gpg --import -
RUN curl -sSL https://rvm.io/pkuczynski.asc | gpg --import -

RUN curl -sSL https://get.rvm.io | bash -s stable --ruby

RUN /usr/local/rvm/bin/rvm install 2.6.3

ENV PATH=/usr/local/rvm/rubies/ruby-2.6.3/bin:$PATH

RUN gem install fastlane -NV 

RUN gem install bundler -NVf 


ENV ANDROID_HOME=/android-sdk-linux
ENV PATH=$PATH:/android-sdk-linux/platform-tools/ 
