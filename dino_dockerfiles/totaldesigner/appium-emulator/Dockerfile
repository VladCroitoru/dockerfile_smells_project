FROM totaldesigner/appium:1.0.0
MAINTAINER totaldesigner <totaldesigner@gmail.com>

#===========================
# Android SDK Manager (API)
#===========================
ENV AVD_VERSION 19
ENV ANDROID_COMPONENTS android-$AVD_VERSION,sys-img-armeabi-v7a-android-$AVD_VERSION
RUN echo y | android update sdk --all --force --no-ui --filter ${ANDROID_COMPONENTS}

#=========================
# Create Android Emulator
#=========================
RUN android create avd --force --name android-$AVD_VERSION --target android-$AVD_VERSION \
  --device "Nexus 5" --abi armeabi-v7a --skin WVGA800

#============================================
# Scripts to run Appium and Android emulator
#============================================
COPY entry_point.sh /opt/bin/entry_point.sh
RUN chmod +x /opt/bin/entry_point.sh

CMD ["/opt/bin/entry_point.sh"]
