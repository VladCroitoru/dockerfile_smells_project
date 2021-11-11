FROM java:8-jdk

RUN apt-get update && apt-get install --yes sudo

# add NodeJS 5.x repo
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -

RUN apt-get update && apt-get install --yes nodejs

# integrated qlik/gradle
ENV GRADLE_VERSION 2.9

VOLUME /project
ENV GRADLE_HOME /gradle
ENV GRADLE_USER_HOME /project/.gradle

WORKDIR /project
RUN curl -sLO https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip && \
  unzip gradle-${GRADLE_VERSION}-all.zip && \
  ln -s gradle-${GRADLE_VERSION} gradle && \
  rm gradle-${GRADLE_VERSION}-all.zip
  
RUN wget https://cli.run.pivotal.io/stable?release=linux64-binary -O /tmp/cf.tgz --no-check-certificate
RUN tar zxf /tmp/cf.tgz -C /usr/bin && chmod 755 /usr/bin/cf

RUN npm install -g gulp

RUN mkdir /build
WORKDIR /build
