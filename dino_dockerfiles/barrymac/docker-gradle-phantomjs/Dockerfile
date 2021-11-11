FROM java:8-jdk
MAINTAINER Barry MacMahon

# Gradle
WORKDIR /usr/bin
RUN wget https://services.gradle.org/distributions/gradle-2.4-all.zip && \
    unzip gradle-2.4-all.zip && \
    ln -s gradle-2.4 gradle && \
    rm gradle-2.4-all.zip

# Set Appropriate Environmental Variables
ENV GRADLE_HOME /usr/bin/gradle
ENV PATH $PATH:$GRADLE_HOME/bin

# Default command is "/usr/bin/gradle -version" on /app dir
# (ie. Mount project at /app "docker --rm -v /path/to/app:/app gradle <command>")
RUN mkdir /app
WORKDIR /app

RUN apt-get update -qq && apt-get upgrade -y && apt-get install -y \
    git \
    build-essential \
    g++ \
    flex \
    bison \
    gperf \
    ruby \
    perl \
    libsqlite3-dev \
    libfontconfig1-dev \
    libicu-dev \
    libfreetype6 \
    libssl-dev \
    libpng-dev \
    libjpeg-dev \
    libqt5webkit5-dev

ENV PHANTOM_JS_TAG 2.0.0

RUN git clone https://github.com/ariya/phantomjs.git /tmp/phantomjs
RUN cd /tmp/phantomjs && git checkout $PHANTOM_JS_TAG && \
  ./build.sh --confirm && mv bin/phantomjs /usr/local/bin

RUN cd /app
