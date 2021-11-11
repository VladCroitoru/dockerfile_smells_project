FROM narfman0/docker-android-sdk

EXPOSE 5037
EXPOSE 5554
EXPOSE 5555
EXPOSE 5900

# install build tools
RUN echo "y" | sdkmanager "platform-tools" "platforms;android-27" "build-tools;27.0.3" && \
    yes | sdkmanager --licenses && \
    chmod -R 777 $ANDROID_HOME

ENV ANDROID_PACKAGE "system-images;android-25;google_apis;armeabi-v7a"
ENV ANDROID_SDK_ROOT=$ANDROID_HOME
ENV PATH $ANDROID_HOME/emulator:$PATH

RUN apt-get install -y libqt5widgets5

# install emulator package
RUN echo "y" | sdkmanager "emulator" $ANDROID_PACKAGE && \
    yes | sdkmanager --licenses && \
    chmod -R 777 $ANDROID_HOME

RUN useradd -ms /bin/bash emulator
USER emulator
WORKDIR /home/emulator

RUN echo "no" | avdmanager create avd -f -k $ANDROID_PACKAGE -n test -b google_apis/armeabi-v7a

ENTRYPOINT ["emulator64-arm", "-avd", "test", "-noaudio", "-no-window", "-ranchu", "-gpu", "off", "-verbose"]
