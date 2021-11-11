FROM gitlab/gitlab-runner:v11.5.0

MAINTAINER Marco Obermeyer "marco.obermeyer@obcon.de"

RUN apt-get update && \
  apt-get install -y software-properties-common && \
  add-apt-repository -y ppa:webupd8team/java && \
  (echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections) && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  apt-get clean && \
  rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*
  ENV JAVA8_HOME /usr/lib/jvm/java-8-oracle
  ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y --force-yes unzip expect git wget libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1 python curl libqt5widgets5 && apt-get clean && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN apt-get update && \
  apt-get -y install python-pip
RUN apt-get -y install libyaml-dev python-dev
RUN pip install awscli boto3

RUN apt-get --quiet update --yes
RUN apt-get --quiet install --yes wget tar unzip lib32stdc++6 lib32z1

RUN wget --quiet --output-document=android-sdk-tools.zip https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
RUN mkdir android-sdk-linux && cd android-sdk-linux && unzip ../android-sdk-tools.zip

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

ENV ANDROID_HOME "/android-sdk-linux"
ENV PATH "${PATH}:/android-sdk-linux/platform-tools:/android-sdk-linux/tools"

# RUN mkdir $ANDROID_HOME/licenses
# RUN echo 8933bad161af4178b1185d1a37fbf41ea5269c55 > $ANDROID_HOME/licenses/android-sdk-license
# RUN echo d56f5187479451eabf01fb78af6dfcb131a6481e >> $ANDROID_HOME/licenses/android-sdk-license
# RUN echo 84831b9409646a918e30573bab4c9c91346d8abd > $ANDROID_HOME/licenses/android-sdk-preview-license

RUN mkdir ${HOME}/.android && touch ${HOME}/.android/repositories.cfg

RUN yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses
RUN $ANDROID_HOME/tools/bin/sdkmanager "tools" "platform-tools"
# RUN $ANDROID_HOME/tools/bin/sdkmanager "build-tools;25.0.3"
RUN $ANDROID_HOME/tools/bin/sdkmanager "build-tools;26.0.2" "build-tools;25.0.3" "build-tools;28.0.3"
RUN $ANDROID_HOME/tools/bin/sdkmanager "platforms;android-25" "platforms;android-28"
# RUN $ANDROID_HOME/tools/bin/sdkmanager "platforms;android-26" "platforms;android-25" "platforms;android-24" "platforms;android-23"
RUN $ANDROID_HOME/tools/bin/sdkmanager "extras;android;m2repository" "extras;google;m2repository"
RUN $ANDROID_HOME/tools/bin/sdkmanager "extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2"
RUN $ANDROID_HOME/tools/bin/sdkmanager "extras;m2repository;com;android;support;constraint;constraint-layout-solver;1.0.2"
RUN $ANDROID_HOME/tools/bin/sdkmanager "extras;google;google_play_services"

RUN yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses

RUN chown -R "gitlab-runner:gitlab-runner" $ANDROID_HOME
