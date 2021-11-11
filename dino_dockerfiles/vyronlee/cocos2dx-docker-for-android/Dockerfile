FROM ubuntu:14.04

MAINTAINER VyronLee <lwz_jz@hotmail.com>

RUN dpkg --add-architecture i386 \
    && dpkg --add-architecture i386 \
    && apt-get update \
    && apt-get install -y libstdc++6:i386 libgcc1:i386 zlib1g:i386 libncurses5:i386 \
    && apt-get install -y python git wget make openjdk-7-jdk
RUN mkdir /android-dev

#=============================
#   download dependences
#=============================

#ant
RUN apt-get -y install ant

#android ndk
RUN wget -P /tmp http://dl.google.com/android/ndk/android-ndk-r10e-linux-x86_64.bin \
    && chmod a+x /tmp/android-ndk-r10e-linux-x86_64.bin
RUN cd /tmp && ./android-ndk-r10e-linux-x86_64.bin \
    && mv /tmp/android-ndk-r10e /android-dev/android-ndk

#android android-dev
RUN wget -P /tmp http://dl.google.com/android/android-sdk_r24.3.1-linux.tgz
RUN tar -vzxf /tmp/android-sdk_r24.3.1-linux.tgz -C /tmp \
    && mv /tmp/android-sdk-linux /android-dev/android-sdk

# 下面的几个id跟上面的http://dl.google.com/android/android-sdk_rXXX-linux.tgz相关，
# 不同的sdk版本会有不同的ID列表，可通过android list sdk -a获取
# 1- Android SDK Tools, revision 24.4.1
# 3- Android SDK Platform-tools, revision 23.1
# 4- Android SDK Build-tools, revision 23.0.2
# 27- SDK Platform Android 5.1.1, API 22, revision 2     <= 注意这里只能用低于Android 5.1.1的版本，更新版本会导致编译失败
RUN echo yes | /android-dev/android-sdk/tools/android update sdk -u -a -t 1,3,4,27

#cleanup
RUN rm -rf /tmp/*

#=============================
#   download frameworks
#=============================
#cocos2dx dev
RUN git clone --depth 1 --branch cocos2d-x-3.10 https://github.com/cocos2d/cocos2d-x.git /cocos2dx
RUN cd /cocos2dx && ./download-deps.py --remove-download yes
RUN cd /cocos2dx && git submodule update --init


#=============================
#   set environments
#=============================
# develop environment
ENV ANDROID_HOME=/android-dev/android-sdk \
    JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/jre \
# Add environment variable NDK_ROOT for cocos2d-x
    NDK_ROOT=/android-dev/android-ndk \
    PATH=$NDK_ROOT:$PATH \
# Add environment variable ANDROID_SDK_ROOT for cocos2d-x
    ANDROID_SDK_ROOT=/android-dev/android-sdk \
    PATH=$ANDROID_SDK_ROOT:$PATH \
    PATH=$ANDROID_SDK_ROOT/tools:$ANDROID_SDK_ROOT/platform-tools:$PATH \
# Add environment variable ANT_ROOT for cocos2d-x
    ANT_ROOT=/usr/bin \
    PATH=$ANT_ROOT:$PATH \
# Add environment variable COCOS_CONSOLE_ROOT for cocos2d-x
    COCOS_CONSOLE_ROOT=/cocos2dx/tools/cocos2d-console/bin \
    PATH=$COCOS_CONSOLE_ROOT:$PATH \
# Add environment variable COCOS_TEMPLATES_ROOT for cocos2d-x
    COCOS_TEMPLATES_ROOT=/cocos2dx/templates \
    PATH=$COCOS_TEMPLATES_ROOT:$PATH \
# Add environment variable COCOS_CONSOLE_ROOT for cocos2d-x
    COCOS_CONSOLE_ROOT=/cocos2dx/tools/cocos2d-console/bin \
    PATH=$COCOS_CONSOLE_ROOT:$PATH \
# Add environment variable COCOS_TEMPLATES_ROOT for cocos2d-x
    COCOS_TEMPLATES_ROOT=/cocos2dx/templates \
    PATH=$COCOS_TEMPLATES_ROOT:$PATH

#entrypoint
WORKDIR /project
ENTRYPOINT ["/cocos2dx/tools/cocos2d-console/bin/cocos"]

