# Scala and sbt Dockerfile
FROM  openjdk:8-jdk-slim

ENV SCALA_VERSION 2.12.12
ENV SBT_VERSION 1.4.1

# Dependecies
RUN apt-get update &&\
    apt-get install -qq -y curl git jq unzip xz-utils libfontconfig zlib1g libfreetype6 libxrender1 libxext6 libx11-6 &&\
    apt-get clean autoremove -y &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

# Install Scala
RUN \
  curl -fsL https://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz | tar xfz - -C /root/ && \
  echo >> /root/.bashrc && \
  echo "export PATH=~/scala-$SCALA_VERSION/bin:$PATH" >> /root/.bashrc

# Install sbt
RUN \
  curl -L -o sbt-$SBT_VERSION.deb https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \
  dpkg -i sbt-$SBT_VERSION.deb && \
  rm sbt-$SBT_VERSION.deb && \
  apt-get update && \
  apt-get -qq -y install sbt && \
  apt-get clean &&\
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* &&\
  sbt -Dsbt.rootdir=true -batch sbtVersion

# Test sbt
RUN \
  mkdir /tmp/sbt &&\
  cd /tmp/sbt &&\
  mkdir -p project project/project src/main/scala &&\
  touch src/main/scala/scratch.scala &&\
  echo "sbt.version=$SBT_VERSION" > project/build.properties &&\
  sbt -batch ++$SCALA_VERSION! clean update compile &&\
  rm -rf /tmp/sbt


# Add jenkins user
RUN \
    adduser --home /var/jenkins_home --disabled-password --uid 1000 jenkins

# Add Wkhtmltopdf
ENV PATH $PATH:/opt/wkhtmltox/bin
ENV WKHTMLTOX_VERSION 0.12.4

RUN curl -L -o wkhtmltopdf.tar.xz  "https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/${WKHTMLTOX_VERSION}/wkhtmltox-${WKHTMLTOX_VERSION}_linux-generic-amd64.tar.xz" &&\
    tar -xvJ -f wkhtmltopdf.tar.xz -C /opt &&\
    rm -rf /opt/wkhtmltox/lib &&\
    rm -rf /opt/wkhtmltox/include &&\
    rm -rf /opt/wkhtmltox/share &&\
    rm wkhtmltopdf.tar.xz

# Define working directory
WORKDIR /root
