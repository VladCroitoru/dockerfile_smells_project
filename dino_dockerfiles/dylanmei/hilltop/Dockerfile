FROM debian:jessie

RUN apt-get update && \
    apt-get install -y curl unzip net-tools && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# JAVA
ENV JAVA_VERSION 1.8.0
ENV JAVA_HOME /usr/jdk1.8.0_31
ENV PATH $PATH:$JAVA_HOME/bin
RUN curl -sL --retry 3 --insecure \
      --header "Cookie: oraclelicense=accept-securebackup-cookie;" \
      "http://download.oracle.com/otn-pub/java/jdk/8u31-b13/server-jre-8u31-linux-x64.tar.gz" \
  | gunzip \
  | tar x -C /usr/ \
 && ln -s $JAVA_HOME /usr/java \
 && rm -rf $JAVA_HOME/man \
 && rm -rf $JAVA_HOME/*src.zip

# GRADLE
ENV GRADLE_VERSION 2.4
ENV GRADLE_HOME /usr/gradle-$GRADLE_VERSION
ENV PATH $PATH:$GRADLE_HOME/bin
RUN curl -sL "https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip" \
      -o /tmp/gradle-$GRADLE_VERSION.zip \
 && unzip /tmp/gradle-$GRADLE_VERSION.zip -d /usr/ \
 && ln -s $GRADLE_HOME /usr/gradle \
 && rm -rf $GRADLE_HOME/plugins \
 && rm -rf $GRADLE_HOME/sonar \
 && rm -rf $GRADLE_HOME/media

ADD . /src
WORKDIR /src

RUN mkdir -p /src/depends \
 && curl -sL "https://s3-us-west-2.amazonaws.com/dylanmei/hilltop/anthill3-dev-kit-5.0.0.2.zip" \
     -o /tmp/anthill3-dev-kit.zip \
 && unzip /tmp/anthill3-dev-kit.zip -d /src/depends/ \
 && gradle installDist \
 && rm -rf /tmp/* /src/depends /src/.gradle

ENV HILLTOP_ANTHILL_API_SERVER ""
ENV HILLTOP_ANTHILL_API_TOKEN ""
ENTRYPOINT ["build/install/src/bin/hilltop"]
