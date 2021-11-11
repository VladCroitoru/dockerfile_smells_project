# Ionic 2 developer container
# Use at your own risk! I have not tested any deployment, created my own as all the others did not work!
# alias ionic="docker run -ti --rm -p 8100:8100 -p 35729:35729 -v \$PWD:/myApp:rw guptasanchit90dev/docker-ionic2:latest ionic"
# then use ionic serve on localhost:8100

FROM ubuntu:16.04

MAINTAINER guptasanchit90dev <gupta.sanchit90@gmail.com>

# Set one or more individual labels
LABEL Description="Ionic 2 Framework Dev container"
LABEL Volumes="/myApp"
LABEL Ports="8100, 35729"
LABEL Ionic_Framework_Version="2.0.0"
LABEL Cordova_CLI_Version="6.5.0"
LABEL Ionic_CLI_Version="2.2.1"
LABEL Ionic_App_Lib_Version="2.2.0"
LABEL Ionic_App_Script_Version="1.0.0"
LABEL Node_Version="7.x"
LABEL TypeScript_Version="2.2.1"
LABEL release-date="2017-03-23"
LABEL is-production="False"
LABEL HOST_ALIAS="alias ionic=docker run -ti --rm -p 8100:8100 -p 35729:35729 -v $PWD:/myApp:rw guptasanchit90dev/docker-ionic2:latest ionic"

RUN apt-get update && apt-get install -y -q curl

RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -

# install nodejs, npm and git
RUN apt-get install -y -q \
            nodejs \
            git \
            && apt-get -y autoclean \
            && rm -rf /var/lib/apt/lists/*

# install ionic, cordova, typescript, gulp
RUN npm install -g -y ionic
RUN npm install -g -y cordova
RUN npm install -g -y typescript
RUN npm install -g -y gulp

RUN echo ' Create a alias for quick launch ...' > /Readme.txt
RUN echo ' alias ionic=docker run -ti --rm -p 8100:8100 -p 35729:35729 -v \$PWD:/myApp:rw bekkere/docker-ionic2:latest ionic' >> /Readme.txt
RUN echo ''
RUN echo ' Installed the following packages:' >> /Readme.txt
RUN echo ' --> Ubuntu 16.04, with curl' >> /Readme.txt
RUN echo ' --> Nodejs version 7.x, git' >> /Readme.txt
RUN echo ' --> NPM install globally ionic, cordova, typescript, gulp' >> /Readme.txt
RUN echo ' ' >> /Readme.txt
RUN echo ' NOTE: Do not run npm update -g npm ... reinstalling npm v3 fails on Docker' >> /Readme.txt

RUN echo 'cd /myApp' > /start.sh
RUN echo 'cat /Readme.txt' >> /start.sh

WORKDIR /myApp

CMD bash -C '/start.sh';'bash'

EXPOSE 8100 35729

# Do NOT use VOLUME statement as it may result in orphaned volumes ...
# docker run --rm ... bash
# VOLUME /myApp
