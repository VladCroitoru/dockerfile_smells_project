#
# Rocketchat Dockerfile
#
# https://github.com/
#

# Pull base image.
FROM debian:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >

ENV ROCKETCHAT_VERSION 4.1.1

# Update & install packages for installing rocketchat
RUN apt-get update && \
    apt-get install -y curl graphicsmagick build-essential wget git

#Add yarn repository
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    curl https://install.meteor.com/ | sh 

# Update & install packages
RUN apt-get update && \
    apt-get install -y npm nodejs

#RUN npm install -g n
#RUN n 0.10.40

#Download Stable version of Rocket.Chat
RUN mkdir Rocket.Chat && \
    cd Rocket.Chat && \
    wget https://api.github.com/repos/RocketChat/Rocket.Chat/tarball/${ROCKETCHAT_VERSION} -O ${ROCKETCHAT_VERSION}.tar.gz && \
    tar xf  ${ROCKETCHAT_VERSION}.tar.gz --strip-components=1 && \
    meteor npm install
#    ls && \
#    mv bundle Rocket.Chat && \i
#    cd Rocket.Chat/programs/server && \
#    cd programs/server && \
#    npm install


CMD ["meteor", " npm", "start"]
