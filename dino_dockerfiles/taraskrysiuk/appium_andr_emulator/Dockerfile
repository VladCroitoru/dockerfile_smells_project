FROM taraskrysiuk/appium_android
MAINTAINER Taras Krysiuk

ENV AVD_VERSION 19
ENV ANDROID_COMPONENTS android-$AVD_VERSION,sys-img-armeabi-v7a-android-$AVD_VERSION
RUN echo y | android update sdk --all --force --no-ui --filter ${ANDROID_COMPONENTS}

RUN android create avd --force --name android-$AVD_VERSION --target android-$AVD_VERSION --device "Nexus S" --abi armeabi-v7a --skin WVGA800

COPY init.sh /opt/bin/init.sh
RUN chmod +x /opt/bin/init.sh

CMD /opt/bin/init.sh