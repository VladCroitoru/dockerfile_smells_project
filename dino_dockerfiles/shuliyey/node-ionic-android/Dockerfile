FROM shuliyey/node-ionic

MAINTAINER Zeyu Ye <Shuliyey@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

ARG VERSION=8
ARG UPDATE=131
ARG BUILD=11
ARG SIG=d54c1d3a095b4ff2b6607d096fa80163

ENV JAVA_HOME /usr/lib/jvm/java-${VERSION}-oracle
ENV JRE_HOME ${JAVA_HOME}/jre

RUN apt-get update && apt-get install unzip -y --no-install-recommends && \
  curl --silent --location --retry 3 --cacert /etc/ssl/certs/GeoTrust_Global_CA.pem \
  --header "Cookie: oraclelicense=accept-securebackup-cookie;" \
  http://download.oracle.com/otn-pub/java/jdk/"${VERSION}"u"${UPDATE}"-b"${BUILD}"/"${SIG}"/jdk-"${VERSION}"u"${UPDATE}"-linux-x64.tar.gz \
  | tar xz -C /tmp && \
  mkdir -p /usr/lib/jvm && mv /tmp/jdk1.${VERSION}.0_${UPDATE} "${JAVA_HOME}" && \
  # Install Java Unlimited Encryption
  curl --silent --location --retry 3 --cacert /etc/ssl/certs/GeoTrust_Global_CA.pem \
    --header "Cookie: oraclelicense=accept-securebackup-cookie;" \
    http://download.oracle.com/otn-pub/java/jce/${VERSION}/jce_policy-${VERSION}.zip \
    -o /tmp/jce_policy-${VERSION}.zip && \
  unzip /tmp/jce_policy-${VERSION}.zip -d /tmp && \
  cp -v /tmp/UnlimitedJCEPolicyJDK${VERSION}/*.jar "${JRE_HOME}"/lib/security/

RUN update-alternatives --install "/usr/bin/java" "java" "${JRE_HOME}/bin/java" 1 && \
  update-alternatives --install "/usr/bin/javaws" "javaws" "${JRE_HOME}/bin/javaws" 1 && \
  update-alternatives --install "/usr/bin/javac" "javac" "${JAVA_HOME}/bin/javac" 1 && \
  update-alternatives --set java "${JRE_HOME}/bin/java" && \
  update-alternatives --set javaws "${JRE_HOME}/bin/javaws" && \
  update-alternatives --set javac "${JAVA_HOME}/bin/javac"

ENV ANDROID_HOME /opt/android-sdk-linux

# Install Android SDK installer
ARG ANDROID_SDK_BUILD=3859397
ARG ANDROID_SDK_SHA256=444e22ce8ca0f67353bda4b85175ed3731cae3ffa695ca18119cbacef1c1bea0
RUN curl -o sdk-tools-linux.zip --cacert /etc/ssl/certs/GeoTrust_Global_CA.pem https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_BUILD}.zip \
  && echo "${ANDROID_SDK_SHA256} sdk-tools-linux.zip" | sha256sum -c \
  && unzip -d /opt/android-sdk-linux sdk-tools-linux.zip \
  && rm *.zip

# Clean Up
RUN apt-get remove --purge --auto-remove -y unzip && \
  apt-get autoclean && apt-get --purge -y autoremove && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["bash"]
