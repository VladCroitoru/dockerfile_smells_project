FROM zanyxdev/dev-java-base:latest

LABEL maintainer "ZanyXDev <zanyxdev@gmail.com>"
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/zanyxdev/dev-android-sdk.git" \
      org.label-schema.vcs-ref=$VCS_REF \
org.label-schema.schema-version="1.0.0-rc1"


RUN curl --create-dirs -L -o /etc/udev/rules.d/51-android.rules -O -L https://raw.githubusercontent.com/snowdream/51-android/master/51-android.rules && \
    chmod a+r /etc/udev/rules.d/51-android.rules

#Installs configure and update Android SDK with components
ENV ANDROID_HOME /opt/android-sdk-linux 
ENV PATH ${PATH}:/opt/android-sdk-linux/tools:/opt/android-sdk-linux/platform-tools
ENV ANDROID_COMPONENTS  platform-tools,android-25, android-22,build-tools-25.0.2, build-tools-22.0.1
ENV GOOGLE_COMPONENTS extra-android-m2repository,extra-google-m2repository,extra-google-google_play_services \
	      extra-google-admob_ads_sdk, extra-google-analytics_sdk_v2, extra-google-google_play_services, \
	      extra-google-market_apk_expansion, extra-google-market_licensing, \
	      extra-google-play_billing, extra-google-webdriver

ENV ANDROID_SOURCE source-22,source-25

#sys-img-x86_64-google_apis-25,sys-img-x86_64-google_apis-25
#ENV GOOGLE_IMG sys-img-x86_64-google_apis-21,sys-img-x86_64-google_apis-22
ENV GOOGLE_APIS addon-google_apis-google-22

RUN curl -L https://dl.google.com/android/repository/tools_r25.2.5-linux.zip -o /tmp/tools_r25.2.5-linux.zip && \
    unzip /tmp/tools_r25.2.5-linux.zip -d $ANDROID_HOME && \
    rm -f /tmp/tools_r25.2.5-linux.zip

RUN mkdir "$ANDROID_HOME/licenses" || true && \
    echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" > "$ANDROID_HOME/licenses/android-sdk-license" && \
    echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" > "$ANDROID_HOME/licenses/android-sdk-preview-license"

RUN echo y | android update sdk --no-ui --all --filter "${ANDROID_COMPONENTS}" && \
    echo y | android update sdk --no-ui --all --filter "${GOOGLE_COMPONENTS}"  && \
    echo y | android update sdk --no-ui --all --filter "${ANDROID_SOURCE}"  && \
    echo y | android update sdk --no-ui --all --filter "${GOOGLE_APIS}" && \
    chown -R developer:developer /opt/android-sdk-linux

# Create fake keymap file
RUN mkdir $ANDROID_HOME/tools/keymaps && \
touch $ANDROID_HOME/tools/keymaps/en-us


#Install specifics for android support - glx drivers etc. \
# Create fake keymap file

#Install Deps
RUN apt-get update && \
    apt-get install -yq --no-install-recommends \
    file \
    apt-utils \
    pciutils \
    expect \
    libc6-i386 \
    lib32stdc++6 \
    lib64stdc++6 \
    libgl1-mesa-glx:i386 \
    mesa-utils \
    lib32gcc1 \
    lib32ncurses5 \
    lib32z1 \
    libqt5widgets5 \
    libgl1-mesa-dev && \    
    apt-get clean && \
    rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*

