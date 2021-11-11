#
# Hubot-rocketchat Dockerfile
#
# https://github.com/
#

# Pull base image.
FROM debian:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >

ENV HUBOT_ROCKETCHAT_VERSION v1.0.11

# Update & install packages for installing rocketchat
RUN apt-get update && \
    apt-get install -y git curl gnupg2 wget && \
    useradd hubot -m

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install -y nodejs

#Download Stable version of Rocket.Chat
RUN mkdir hubot-rocketchat && \
    cd hubot-rocketchat && \
    wget https://api.github.com/repos/RocketChat/hubot-rocketchat/tarball/${HUBOT_ROCKETCHAT_VERSION} -O ${HUBOT_ROCKETCHAT_VERSION}.tar.gz && \
    tar xf  ${HUBOT_ROCKETCHAT_VERSION}.tar.gz --strip-components=1 && \
    npm install -g coffee-script yo generator-hubot


USER hubot
RUN cd /home/hubot/ && \
    mkdir myhubot && \
    cd myhubot && \
    yo hubot -f --no-insight --owner="Hihouhou <hihouhou@hihouhou.com>" --name="hihouhou" --description="Bot" --adapter="rocketchat" 

WORKDIR /home/hubot/myhubot/

CMD ["./bin/hubot", "-a", "rocketchat"]
