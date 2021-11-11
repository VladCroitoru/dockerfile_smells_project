# Node based image with Yarn, Gulp, Grunt, Bower, Gatsby, rsync, lftp components
FROM node:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

RUN apt-get update && apt-get install -y \
    apt-transport-https \
    git \
    zip \
    unzip \
    rsync \
    lftp

# Add yarn repository
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update \
    && apt-get install -y yarn \
    && npm install -g gulp-cli \
    && npm install -g grunt-cli \
    && npm install -g gatsby-cli \
    && npm install -g bower

ENV DEBIAN_FRONTEND teletype

CMD ["node", "npm", "bower", "gulp", "yarn"]
