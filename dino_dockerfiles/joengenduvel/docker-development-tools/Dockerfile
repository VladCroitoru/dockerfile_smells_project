FROM joengenduvel/docker-x11-client

# Developer tools
RUN apk add --no-cache git nodejs nodejs-npm ruby ruby-dev python2 make gcc g++ gnupg bzip2 openjdk8
RUN gem install sass --no-doc --clear-sources
RUN npm install -g gulp bower polymer-cli --unsafe-perm --clear-sources generator-polymer-init-custom-build grunt-cli 

WORKDIR /root
