FROM ubuntu:14.04

# let's setup all the necessary environment variables
ENV BUILD_HOME=/build
ENV APP_DIR=/opt/dropwizard

# Install Java.
RUN \
  apt-get update && \
  apt-get install -y software-properties-common && \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  apt-get install -y maven && \
  apt-get install -y git && \
  mkdir $BUILD_HOME && \
  cd $BUILD_HOME && \
  git clone https://github.com/nickdala/AliveSince.git && \
  cd AliveSince && \
  mvn package && \
  mkdir $APP_DIR && \
  cp target/dropwizard-app-1.0-SNAPSHOT.jar $APP_DIR && \
  cp config.yml $APP_DIR && \
  cd && rm -rf $BUILD_HOME && \
  apt-get -y autoremove maven && \
  apt-get -y autoremove git && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer

EXPOSE 8080

WORKDIR /opt/dropwizard
CMD ["java", "-jar", "dropwizard-app-1.0-SNAPSHOT.jar", "server", "config.yml"]
