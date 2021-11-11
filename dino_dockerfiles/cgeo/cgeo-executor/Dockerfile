FROM ubuntu:xenial

RUN apt-get update \
    && apt-get -y install \
        openjdk-8-jdk-headless \
        wget \
        curl \
        unzip \
        lib32stdc++6 \
        libqt5widgets5 \
        lib32z1 \
        tzdata \
        git \
        vim \
        less \
        bind9-host \
        iputils-ping \
        supervisor \
        qemu-kvm \
        sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV SDK_VERSION=4333796
ENV ANDROID_HOME=/opt/android-sdk-linux/
ENV PATH=$PATH:/opt/android-sdk-linux/tools/:/opt/android-sdk-linux/tools/bin/:/opt/android-sdk-linux/platform-tools/
ENV QEMU_AUDIO_DRV=none

COPY android-packages /tmp/

RUN wget -O /tmp/sdk-tools-linux.zip https://dl.google.com/android/repository/sdk-tools-linux-${SDK_VERSION}.zip \
    && unzip /tmp/sdk-tools-linux.zip -d /opt/android-sdk-linux/ \
    && rm -f /tmp/sdk-tools-linux.zip \
    && mkdir -p /var/log/supervisor \
    && yes | sdkmanager --licenses \
    && while read p; do echo "y" | sdkmanager "${p}"; done </tmp/android-packages \
    && yes | sdkmanager --update \
    && yes | sdkmanager --licenses \
    && useradd -m jenkins \
    && chown -R jenkins. /opt/android-sdk-linux/ \
    && cd /opt/android-sdk-linux/platform-tools/ \
    && mv adb adb.orig \
    && ln -s /usr/local/bin/adb+ adb \
    && chown jenkins. /var/log/supervisor

COPY scripts/* /usr/local/bin/
# To be compatible with old Jenkins scripts
COPY scripts/restart-emulator.sh /home/jenkins/restart-emulator.sh

COPY emulators.conf /etc/supervisor/conf.d/emulators.conf

WORKDIR /home/jenkins
CMD ["/usr/local/bin/start.sh"]

#RUN avdmanager --verbose create avd -c 50M -k "system-images;android-19;google_apis;x86" -n android-19 -g google_apis -b x86 -d "Nexus 4" \
#    && avdmanager --verbose create avd -c 50M -k "system-images;android-22;google_apis;x86_64" -n android-22 -g google_apis -b x86_64 -d "Nexus 4" \
#    && avdmanager --verbose create avd -c 50M -k "system-images;android-23;google_apis;x86_64" -n android-23 -g google_apis -b x86_64 -d "Nexus 4" \
#    && avdmanager --verbose create avd -c 50M -k "system-images;android-24;google_apis;x86_64" -n android-24 -g google_apis -b x86_64 -d "Nexus 4" \
#    && avdmanager --verbose create avd -c 50M -k "system-images;android-25;google_apis;x86_64" -n android-25 -g google_apis -b x86_64 -d "Nexus 4" \
#    && avdmanager --verbose create avd -c 50M -k "system-images;android-26;google_apis;x86" -n android-26 -g google_apis -b x86 -d "Nexus 4"


# Launch with:
#  docker run -d --privileged --name cgeo-executor -v PATH-TO-YOUR-SRV:/srv cgeo-executor
#
# The local srv directory must contain:
#  - slave: the name of the Jenkins slave
#  - secret: the secret of the Jenkins slave
#  - private.properties
#  - cgeo.geocaching_preferences.xml
#
# Your user must have access to /dev/kvm
