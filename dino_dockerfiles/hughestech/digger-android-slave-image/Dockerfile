FROM openshift/jenkins-slave-base-centos7

MAINTAINER AeroGear Team <https://aerogear.org/>

#env vars
ENV ANDROID_SLAVE_SDK_BUILDER=1.0.0 \
    NODEJS_DEFAULT_VERSION=6.9.1 \
    CORDOVA_DEFAULT_VERSION=7.1.0 \
    GRUNT_DEFAULT_VERSION=1.0.1 \
    FASTLANE_DEFAULT_VERSION=2.69.2 \
    GRADLE_VERSION=4.4 \
    ANDROID_HOME=/opt/android-sdk-linux \
    NVM_DIR=/opt/nvm \
    PROFILE=/etc/profile \
    CI=Y \
    BASH_ENV=/etc/profile \
    JAVA_HOME=/etc/alternatives/java_sdk_1.8.0

#update PATH env var
ENV PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$NVM_DIR:/opt/gradle/gradle-$GRADLE_VERSION/bin

LABEL io.k8s.description="Platform for building slave android sdk image" \
      io.k8s.display-name="jenkins android sdk slave builder" \
      io.openshift.tags="jenkins-android-slave builder"

#system pakcages
RUN yum install -y \
  zlib.i686 \
  ncurses-libs.i686 \
  bzip2-libs.i686 \
  java-1.8.0-openjdk-devel \
  java-1.8.0-openjdk \
  ruby \
  rubygems \
  ruby-devel \
  nodejs \
  gcc-c++ \
  make \
  ant \
  which\
  wget \
  expect && \
  yum groupinstall -y "Development Tools"

#install nvm and nodejs


# install nvm
# https://github.com/creationix/nvm#install-script
RUN curl --silent -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.7/install.sh | bash

# install node and npm
RUN source $NVM_DIR/nvm.sh \
    && nvm install $NODEJS_DEFAULT_VERSION \
    && nvm alias default $NODEJS_DEFAULT_VERSION \
    && nvm use default

# add node and npm to path so the commands are available
ENV NODE_PATH $NVM_DIR/v$NODEJS_DEFAULT_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODEJS_DEFAULT_VERSION/bin:$PATH




RUN npm install -g cordova@${CORDOVA_DEFAULT_VERSION} && \
    npm install -g grunt@${GRUNT_DEFAULT_VERSION}  && \
    npm install -g exp && \
    gem install bundler && gem install rubygems-update && \
    update_rubygems && gem install jwt -v 1.5.6 && gem install fastlane -NV --verbose && \

#install gradle
    mkdir -p /opt/gradle && \
    wget https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip && \
    unzip -d /opt/gradle gradle-${GRADLE_VERSION}-bin.zip && \
    rm gradle-${GRADLE_VERSION}-bin.zip && \

#install jq
    wget -O jq  https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 && \
    chmod +x ./jq &&\
    cp jq /usr/bin

#fix permissions
RUN mkdir -p $HOME/.android && \
    touch $HOME/.android/analytics.settings && \
    touch $HOME/.android/reposiories.cfg && \
    # create a symlink for the debug.keystore (source: $ANDROID_HOME/android.debug, target: $HOME/.android/debug.keystore)
    # $ANDROID_HOME/android.debug file currently doesn't exist in this image.
    # it will be there once the android-sdk volume is mounted (later in OpenShift).
    # the good thing about symlinks are that they can be created even when the source doesn't exist.
    # when the source becomes existent, it will just work.
    ln -s $ANDROID_HOME/android.debug $HOME/.android/debug.keystore && \
    chown -R 1001:0 $HOME && \
    chmod -R g+rw $HOME

COPY scripts/run-jnlp.sh /usr/local/bin/run-jnlp.sh

USER 1001
WORKDIR /tmp

ENTRYPOINT ["/usr/local/bin/run-jnlp.sh"]
