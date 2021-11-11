#
# Android Docker v1.0
#
# https://hub.docker.com/r/randr0id/android-docker
# https://github.com/randr0id/android-docker
#

FROM ubuntu:18.04
LABEL maintainer="randy@randr0id.com"

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.name="randr0id/android-docker"
LABEL org.label-schema.description="A Docker image for building and testing Android apps."
LABEL org.label-schema.version="1.0"
LABEL org.label-schema.build-date=${BUILD_DATE}
LABEL org.label-schema.url="https://hub.docker.com/r/randr0id/android-docker"
LABEL org.label-schema.vcs-url="https://github.com/randr0id/android-docker"
LABEL org.label-schema.vcs-ref=${VCS_REF}

ENV VERSION_TOOLS "6858069"

ENV ANDROID_HOME "/sdk"
ENV PATH "${PATH}:${ANDROID_HOME}/tools"
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update && \
    apt-get install -qqy --no-install-recommends \
        build-essential=12.4ubuntu1 \
        bzip2=1.0.6-8.1ubuntu0.2 \
        curl=7.58.0-2ubuntu3.12 \
        git=1:2.17.1-1ubuntu0.7 \
        html2text=1.3.2a-21 \
        libc6-i386=2.27-3ubuntu1.4 \
        lib32stdc++6=8.4.0-1ubuntu1~18.04 \
        lib32gcc1=1:8.4.0-1ubuntu1~18.04 \
        lib32ncurses5=6.1-1ubuntu1.18.04 \
        lib32z1=1:1.2.11.dfsg-0ubuntu2 \
        openjdk-8-jdk=8u275-b01-0ubuntu1~18.04 \
        qemu-kvm=1:2.11+dfsg-1ubuntu7.34 \
        unzip=6.0-21ubuntu1.1 \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN rm -f /etc/ssl/certs/java/cacerts; \
    /var/lib/dpkg/info/ca-certificates-java.postinst configure

RUN curl -s https://dl.google.com/android/repository/commandlinetools-linux-${VERSION_TOOLS}_latest.zip > /tools.zip && \
    unzip /tools.zip -d ${ANDROID_HOME} && \
    mv ${ANDROID_HOME}/cmdline-tools ${ANDROID_HOME}/tools && \
    rm -v /tools.zip

RUN mkdir -p ${ANDROID_HOME}/licenses/ && \
    printf "8933bad161af4178b1185d1a37fbf41ea5269c55\\nd56f5187479451eabf01fb78af6dfcb131a6481e\\n24333f8a63b6825ea9c5514f83c2829b004d1fee" > ${ANDROID_HOME}/licenses/android-sdk-license && \
    printf "84831b9409646a918e30573bab4c9c91346d8abd\\n504667f4c0de7af1a06de9f4b1727b84351f2910" > ${ANDROID_HOME}/licenses/android-sdk-preview-license

RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager --sdk_root=${ANDROID_HOME} --licenses

RUN mkdir -p /root/.android && \
    touch /root/.android/repositories.cfg && \
    ${ANDROID_HOME}/tools/bin/sdkmanager --sdk_root=${ANDROID_HOME} --update

COPY packages.txt ${ANDROID_HOME}
RUN while read -r package; do PACKAGES="${PACKAGES}${package} "; done < /sdk/packages.txt && \
    ${ANDROID_HOME}/tools/bin/sdkmanager --sdk_root=${ANDROID_HOME} ${PACKAGES}

COPY utils ${ANDROID_HOME}/utils

RUN chmod +070 ${ANDROID_HOME}

WORKDIR /work
