FROM ubuntu:14.04
MAINTAINER Fabian Schulte <fabian.schulte@neomatt.de>

# Install Node
RUN apt-get update
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN apt-get update && \
	apt-get install -y nodejs build-essential libfontconfig libfreetype6 libfontconfig1-dev libssl-dev libxft-dev automake autoconf git && \
	apt-get clean

# Install Yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
RUN sudo apt-get update && sudo apt-get install yarn

# Global deps
RUN npm install -g ember-cli@2.12.3 phantomjs@1.9.8 bower@1.7.1 xo cordova-icon@0.13.0 cordova-splash@0.12.0 lodash@">=4.3.0" elementtree@">=0.1.6" plist@">=1.2.0" xcode@">=0.8.9" colors@">=1.1.2" shelljs@">=0.7.0" tostr@">=0.1.0" jshint@">=2.6.0" got@">=6.5.0"
RUN npm config set loglevel error --global

RUN echo '{ "allow_root": true }' > /root/.bowerrc

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

CMD ["npm", "start"]
