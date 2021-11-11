FROM jetbrains/teamcity-agent:10.0.3
MAINTAINER Julien Enocq <julien@enocq.fr>

ENV USER buildagent
ENV ANDROID_HOME /opt/android-sdk-linux
ENV ANDROID_SDK_TOOLS_REVISION 24.4.1
ENV ANDROID_NDK_REVISION 13b
ENV ANDROID_NDK /opt/android-ndk-r${ANDROID_NDK_REVISION}
ENV OPEN_CV_ANDROID_SDK_REVISION 2.4.13
ENV OPEN_CV_ROOT /opt/opencv-${OPEN_CV_ANDROID_SDK_REVISION}

# Prepare the build agent to start as the buildagent user
RUN apt-get install --no-install-recommends -y sudo git git-crypt \
 && chown -R $USER:$USER /opt/buildagent \
 && sed -i 's/${AGENT_DIST}\/bin\/agent.sh start/sudo -Eu buildagent ${AGENT_DIST}\/bin\/agent.sh start/' \
    /run-agent.sh

# Import the Let's Encrypt Authority certificate for Java to accept TeamCity server certificate
RUN curl -o /root/lets-encrypt.der https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.der \
 && $JRE_HOME/bin/keytool -trustcacerts -keystore $JRE_HOME/lib/security/cacerts -storepass changeit \
    -noprompt -importcert -alias lets-encrypt-x3-cross-signed -file /root/lets-encrypt.der \
 && rm /root/lets-encrypt.der

# Install Android command line tools
RUN curl https://dl.google.com/android/android-sdk_r${ANDROID_SDK_TOOLS_REVISION}-linux.tgz | tar xz -C /opt \
 && chown -R $USER:$USER $ANDROID_HOME

# Install Android licenses to not accept them manually during builds
ADD licenses.tar.gz $ANDROID_HOME/

# Install Android extra repos
RUN echo y | sudo -u $USER $ANDROID_HOME/tools/android update sdk --no-ui --all --filter \
extra-android-m2repository,extra-google-m2repository

# Install Android NDK
RUN curl https://dl.google.com/android/repository/android-ndk-r${ANDROID_NDK_REVISION}-linux-x86_64.zip -o android-ndk.zip \
 && unzip android-ndk.zip -d /opt \
 && chown -R $USER:$USER $ANDROID_NDK \
 && rm android-ndk.zip

 # Install OpenCV android sdk
RUN curl -Lk https://github.com/Itseez/opencv/archive/${OPEN_CV_ANDROID_SDK_REVISION}.zip -o opencv.zip \
 && unzip opencv.zip -d /opt \
 && chown -R $USER:$USER $OPEN_CV_ROOT \
 && rm opencv.zip
