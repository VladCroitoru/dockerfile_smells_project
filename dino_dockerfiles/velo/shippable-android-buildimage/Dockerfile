FROM drydock/u14jav:prod

RUN apt-get update -qq ; apt-get install -qq lib32stdc++6 lib32z1 ; apt-get clean

RUN wget http://dl.google.com/android/android-sdk_r24.3.4-linux.tgz ; tar -zxf android-sdk_r24.3.4-linux.tgz ; rm android-sdk_r24.3.4-linux.tgz

ENV ANDROID_HOME=/android-sdk-linux
ENV PATH "/android-sdk-linux/tools:/android-sdk-linux/platform-tools:$PATH"

RUN echo "y" | android update sdk -a --filter platform-tools --no-ui --force
RUN echo "y" | android update sdk -a --filter build-tools-23.0.3 --no-ui --force
# RUN echo "y" | android update sdk -a --filter tools --no-ui --force
RUN echo "y" | android update sdk -a --filter android-23 --no-ui --force
RUN echo "y" | android update sdk -a --filter extra --no-ui --force
