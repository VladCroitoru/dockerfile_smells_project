FROM        ubuntu:trusty
MAINTAINER  Richard Drake <richard.drake@uoit.ca>

# Expose the SS port
EXPOSE      4567

# These should be set with -e when running the container
ENV         SS_USERNAME     username
ENV         SS_CONSUMER_KEY public
ENV         SS_CONSUMER_SEC secret
ENV         SS_TOKEN        public
ENV         SS_TOKEN_SEC    secret

# Enable installation of the Oracle JDK without user interaction
RUN         apt-get update && apt-get install -y \
  software-properties-common \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/*
RUN         add-apt-repository -y ppa:webupd8team/java
RUN         echo oracle-java8-installer \
  shared/accepted-oracle-license-v1-1 select true | \
  sudo /usr/bin/debconf-set-selections

RUN         apt-get update && apt-get install -y \
  maven \
  git \
  oracle-java8-installer \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/*

# Fetch the latest version of the code
RUN         git clone https://github.com/vialab/sentiment-state.git \
  /usr/src/sentiment-state

WORKDIR     /usr/src/sentiment-state

# Build code and create JAR file
RUN         mvn package

# This may or may not remove the Maven cache
RUN         rm -rf /root/.m2

ENTRYPOINT  ["java", "-jar", "vialab/target/vialab-0.0.1-SNAPSHOT-jar-with-dependencies.jar"]
