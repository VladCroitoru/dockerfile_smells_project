FROM node:7.10.0
MAINTAINER bennettaur <mbennett@stunlocksecurity.com>

ENV GATSBY_VERSION ^0.12.45

# Global install yarn package manager
RUN apt-get update && apt-get install -y curl apt-transport-https && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && apt-get install -y yarn && npm install -g gatsby@${GATSBY_VERSION}

