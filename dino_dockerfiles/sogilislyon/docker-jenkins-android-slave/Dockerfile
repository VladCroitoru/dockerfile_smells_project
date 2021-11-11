FROM beevelop/java

MAINTAINER Sylvain Bonnard <sylvainb@sogilis.com>

ENV  ANDROID_SDK_URL "https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz"
ENV  ANDROID_BUILD_TOOLS_VERSION 24.0.1
ENV  ANDROID_APIS "android-23"
ENV  ANT_HOME "/usr/share/ant"
ENV  MAVEN_HOME "/usr/share/maven"
ENV  GRADLE_HOME "/usr/share/gradle"
ENV  ANDROID_HOME "/opt/android-sdk-linux"

ENV DEBIAN_FRONTEND noninteractive

ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/$ANDROID_BUILD_TOOLS_VERSION:$ANT_HOME/bin:$MAVEN_HOME/bin:$GRADLE_HOME/bin

RUN dpkg --add-architecture i386 && \
    apt-get -qq update && \
    apt-get -qq install -y curl ant gradle libncurses5:i386 libstdc++6:i386 zlib1g:i386

    # Installs Android SDK
RUN curl -sL ${ANDROID_SDK_URL} | tar xz -C /opt && \
    echo "y" | android update sdk -u -a -t platform-tools,${ANDROID_APIS},build-tools-${ANDROID_BUILD_TOOLS_VERSION} && \
    echo "y" | android update sdk -u -a -t extra-android-support && \
    echo "y" | android update sdk -u -a -t sys-img-armeabi-v7a-${ANDROID_APIS} && \
    echo "y" | android update sdk -u -a -t extra-android-m2repository && \
    echo "y" | android update sdk -u -a -t extra-google-google_play_services && \
    echo "y" | android update sdk -u -a -t extra-google-gcm && \
    chmod a+x -R $ANDROID_HOME && \

    # Clean up
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get autoremove -y && \
    apt-get clean

# Install a basic SSH server
RUN apt-get update
RUN apt-get install -y openssh-server
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN mkdir -p /var/run/sshd

# Install packages needed for the build
RUN apt-get install -y --no-install-recommends git maven

RUN adduser --quiet jenkins
RUN echo "jenkins:jenkins" | chpasswd
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
