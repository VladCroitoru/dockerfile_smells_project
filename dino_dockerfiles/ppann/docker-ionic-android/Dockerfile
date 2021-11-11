FROM ppann/docker-android-sdk

ENV CORDOVA_VERSION=6.5.0 \
    IONIC_VERSION=3.5.0 \
    GRADLE_VERSION=2.14.1\
    GRADLE_HOME=/opt/gradle-2.14.1

##
# ESSENTIALS
# - GIT: Disable SSL verification for all repositories
##
RUN apt-get update && \
    apt-get install -y wget curl unzip && \
    apt-get install -y -q python-software-properties software-properties-common && \
    apt-get install -y apt-transport-https build-essential git && \
    git config --global http.sslVerify false

##
# GRADLE
##
RUN cd /opt && \
    wget -q https://services.gradle.org/distributions/gradle-"$GRADLE_VERSION"-all.zip && \
    unzip -q gradle-"$GRADLE_VERSION"-all.zip
ENV PATH ${PATH}:${GRADLE_HOME}/bin

# https://stackoverflow.com/a/37732545/3841188
# Point to /opt/gradle-2.14.1-all.zip
ENV CORDOVA_ANDROID_GRADLE_DISTRIBUTION_URL file\:/opt/gradle-"$GRADLE_VERSION"-all.zip

##
# PHANTOMJS
# - Found solution on https://gist.github.com/julionc/7476620
# - Install these packages needed by PhantomJS to work correctly.
##
RUN apt-get install -y --force-yes build-essential chrpath libssl-dev libxft-dev && \
    apt-get install -y --force-yes libfreetype6 libfreetype6-dev && \
    apt-get install -y --force-yes libfontconfig1 libfontconfig1-dev

##
# NODEJS
##
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && \
    apt-get install -y nodejs

##
# CORDOVA / IONIC
##
RUN npm install -g \
    cordova@"$CORDOVA_VERSION" \
    ionic@"$IONIC_VERSION" \
    phantomjs-prebuilt

RUN cordova telemetry off && \
    apt-get clean


###
#   AWS CLI
###

RUN apt-get update && apt-get install -y \
    python-pip \
    groff \
    maven && \
    pip install awscli
