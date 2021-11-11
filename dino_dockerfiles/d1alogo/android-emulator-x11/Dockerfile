FROM ubuntu:xenial
MAINTAINER Pin <pinfake@hotmail.com>
EXPOSE 5037 5554 5555
EXPOSE 8484
RUN apt-get update && \
    apt-get install -y curl default-jre-headless libgl1-mesa-glx unzip libpulse0 && \
    apt-get clean

RUN cd /tmp && \
    curl -O https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip && \
    cd /opt && mkdir android-sdk-linux && cd android-sdk-linux  && unzip /tmp/*.zip && rm /tmp/*.zip 

ENV ANDROID_HOME="/opt/android-sdk-linux"
ENV LD_LIBRARY_PATH="${ANDROID_HOME}/tools/lib"
ENV ANDROID_SDK_HOME="${ANDROID_HOME}"
ENV PATH="${ANDROID_HOME}/emulator:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools:${PATH}"
ENV LD_LIBRARY_PATH="${ANDROID_HOME}/tools/lib:${ANDROID_HOME}/emulator/lib64:${ANDROID_HOME}/emulator/lib64/qt/lib:${ANDROID_HOME}/emulator/lib/libstdc++"
#ENV PATH="${PATH}:${ANDROID_SDK_HOME}/tools"

#RUN echo "y" | sdkmanager --list --verbose
COPY extra_files/repositories.cfg $ANDROID_HOME/.android/
RUN echo "y" | sdkmanager "tools"
RUN echo "y" | sdkmanager "emulator"
RUN echo "y" | sdkmanager "sources;android-24"
RUN echo "y" | sdkmanager "platforms;android-24"
RUN echo "y" | sdkmanager "system-images;android-24;google_apis;x86_64"
RUN echo "n" | avdmanager create avd --force -n nexus7  -b google_apis/x86_64 -k "system-images;android-24;google_apis;x86_64"
COPY avd7/config.ini $ANDROID_HOME/.android/avd/nexus7.avd/

RUN echo "y" | apt-get install pulseaudio
ENV PULSE_SERVER /run/pulse/native

COPY extra_files/skins.zip $ANDROID_HOME/
RUN cd /opt/android-sdk-linux && unzip skins.zip && rm skins.zip 

RUN echo "y" | sdkmanager "system-images;android-26;google_apis_playstore;x86"
RUN echo "n" | avdmanager create avd --force -n nexusPlaystore8  -b google_apis_playstore/x86 -k "system-images;android-26;google_apis_playstore;x86"
COPY avd8Playstore/config.ini $ANDROID_HOME/.android/avd/nexusPlaystore8.avd/

RUN echo "y" | sdkmanager "system-images;android-26;google_apis;x86"
RUN echo "n" | avdmanager create avd --force -n nexus8  -b google_apis/x86 -k "system-images;android-26;google_apis;x86"
COPY avd8/config.ini $ANDROID_HOME/.android/avd/nexus8.avd/

RUN echo "y" | sdkmanager "system-images;android-27;google_apis;x86"
RUN echo "n" | avdmanager create avd --force -n nexus8_1  -b google_apis/x86 -k "system-images;android-27;google_apis;x86"
COPY avd8_1/config.ini $ANDROID_HOME/.android/avd/nexus8_1.avd/


#run emulator -netdelay none -netspeed full -avd Galaxy_Nexus_API_24
ENTRYPOINT ["emulator","@nexus8_1"]


