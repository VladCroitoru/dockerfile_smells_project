#
# Ubuntu Dockerfile
#
# https://github.com/dockerfile/ubuntu
#

# Pull base image.
FROM ubuntu:14.04

# Install.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget make ca-certificates && \
  rm -rf /var/lib/apt/lists/*

# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

# Define default command.
CMD ["bash"]
RUN apt-get update

# Install cloudfoundry-cli
RUN curl -L "https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" | tar -zx
RUN mv cf /usr/local/bin

# Install app dependencies
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && apt-get install -qy g++ gcc python nodejs && \
  npm install --quiet node-gyp -g
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - 
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -qy google-chrome-stable
RUN apt-get update && \
    apt-get upgrade -y && \
    add-apt-repository ppa:openjdk-r/ppa && apt-get update && apt-get install -qy openjdk-8-jdk && \
    update-alternatives --config java && \
	apt-get clean

# install sonar scanner
RUN wget -q -O sonarscanner.zip https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-2.8.zip
RUN unzip sonarscanner.zip
RUN rm sonarscanner.zip

ENV SONAR_RUNNER_HOME=/root/sonar-scanner-2.8
ENV PATH $PATH:/root/sonar-scanner-2.8/bin

# Install JQ
ENV JQ_VERSION='1.5'
RUN wget --no-check-certificate https://raw.githubusercontent.com/stedolan/jq/master/sig/jq-release.key -O /tmp/jq-release.key && \
    wget --no-check-certificate https://raw.githubusercontent.com/stedolan/jq/master/sig/v${JQ_VERSION}/jq-linux64.asc -O /tmp/jq-linux64.asc && \
    wget --no-check-certificate https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}/jq-linux64 -O /tmp/jq-linux64 && \
    gpg --import /tmp/jq-release.key && \
    gpg --verify /tmp/jq-linux64.asc /tmp/jq-linux64 && \
    cp /tmp/jq-linux64 /usr/bin/jq && \
    chmod +x /usr/bin/jq && \
    rm -f /tmp/jq-release.key && \
    rm -f /tmp/jq-linux64.asc && \
    rm -f /tmp/jq-linux64

#Install bower, gulp, jspm, grunt, protractor
RUN npm install -g bower
RUN npm install -g gulp
RUN npm install -g jspm
RUN npm install -g grunt-cli
RUN npm install -g grunt@0.4.4
RUN npm install -g grunt-shell-spawn@0.3.10
RUN npm install -g grunt-protractor-runner@3.2.0
RUN npm install -g grunt-protractor-webdriver
