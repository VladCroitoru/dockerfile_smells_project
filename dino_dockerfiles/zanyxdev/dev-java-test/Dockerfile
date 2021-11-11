FROM ubuntu:latest 
MAINTAINER ZanyXDev <zanyxdev@gmail.com>

# Dependencies
RUN dpkg --add-architecture i386 \
    && apt-get update \
    && apt-get install -y --no-install-recommends software-properties-common \
    && add-apt-repository ppa:openjdk-r/ppa \
    && apt-get update \
    && apt-get install -yq --no-install-recommends \
	libstdc++6:i386 \
	zlib1g:i386 \
	libncurses5:i386 \
	curl \
	sudo \
	unzip \
	openjdk-8-jdk \
	ca-certificates-java \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*
# fix default setting
#ln -s java-8-openjdk-amd64 /usr/lib/jvm/default-jvm

# set default java environment variable
ENV JAVA_VERSION_MAJOR=8 \
    JAVA_VERSION_MINOR=111 \
    JAVA_HOME=/usr/lib/jvm/default-jvm \
    ANDROID_HOME=$HOME/android-sdk-linux

ENV PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:/usr/lib/jvm/default-jvm/bin/
ENV DISPLAY :0

#set Russian locale
ENV LC_ALL ru_RU.UTF-8 
ENV LANG ru_RU.UTF-8 
ENV LANGUAGE ru_RU.UTF-8 
#RUN locale-gen ru_RU.UTF-8

# Development user
RUN echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \
    && useradd -u 1000 -G sudo -d /home/developer --shell /bin/bash -m developer \
    && echo "secret\nsecret" | passwd developer

ENV HOME /home/developer 

RUN mkdir -m 700 /data && \
    mkdir -m 700 $HOME/.AndroidStudio2.2 && \
    mkdir -m 700 $HOME/AndroidStudioProjects && \
    chown -R developer:developer /data $HOME/.AndroidStudio2.2 $HOME/AndroidStudioProjects

ENV GRADLE_URL http://services.gradle.org/distributions/gradle-3.3-all.zip
RUN curl -L ${GRADLE_URL} -o /tmp/gradle-3.3-all.zip && unzip /tmp/gradle-3.3-all.zip -d /usr/local && rm /tmp/gradle-3.3-all.zip

# Set things up using the dev user and reduce the need for `chown`s
USER developer

ENV GRADLE_HOME /usr/local/gradle-3.3

#Installs Android SDK
RUN curl -L https://dl.google.com/android/repository/tools_r25.2.3-linux.zip -o /tmp/tools_r25.2.3-linux.zip \
    && unzip /tmp/tools_r25.2.3-linux.zip -d /home/developer/android-sdk-linux \
    && rm -f /tmp/tools_r25.2.3-linux.zip

#Installs Android Studio
ENV ANDROID_STUDIO_FILENAME android-studio-ide-145.3537739-linux.zip
ENV ANDROID_STUDIO_URL https://dl.google.com/dl/android/studio/ide-zips/2.2.3.0/${ANDROID_STUDIO_FILENAME}
ENV ANDROID_STUDIO_HOME /home/developer/android-studio

RUN mkdir -p ${ANDROID_STUDIO_HOME}  && \
    curl -L ${ANDROID_STUDIO_URL} -o /home/developer/${ANDROID_STUDIO_FILENAME} &&\
    unzip -q /home/developer/${ANDROID_STUDIO_FILENAME} -d /home/developer && \
    rm -f  /home/developer/${ANDROID_STUDIO_FILENAME} && \
    chown -R developer:developer ${ANDROID_STUDIO_HOME}

# Configure the SDK
# TODO: Move this up so that it is cached between android-studio releases
ENV ANDROID_HOME="/home/developer/android-sdk-linux" \
    PATH="${PATH}:/home/developer/android-sdk-linux/tools:/home/developer/android-sdk-linux/platform-tools" \
    JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"

RUN echo y | android update sdk --all --no-ui --force --filter android-22
RUN echo y | android update sdk --all --no-ui --force --filter platform-tools
RUN echo y | android update sdk --all --no-ui --force --filter extra-android-m2repository
RUN echo y | android update sdk --all --no-ui --force --filter extra-google-m2repository
RUN echo y | android update sdk --all --no-ui --force --filter source-22
RUN echo y | android update sdk --all --no-ui --force --filter build-tools-22.0.1
RUN echo y | android update sdk --all --no-ui --force --filter android-21
RUN echo y | android update sdk --all --no-ui --force --filter build-tools-21.1.2

WORKDIR /home/developer/

# Make info file about this build
# printf "Build of zanyxdev/dev-java:0.1, date: %s\n"  `date -u +"%Y-%m-%dT%H:%M:%SZ"` > /var/log/java_install

CMD /home/developer/android-studio/bin/studio.sh
