FROM ubuntu:16.04

LABEL maintainer="Tetsuo Seto <setogit@gmail.com>"

# Get basic tools
RUN apt-get update && apt-get install -y --no-install-recommends \
        curl

# Get git and Nodejs including npm
# CAUTION: Node is installed as "nodejs": 4.2.6
# CAUSION: Use strict mode in runtime: --use_strict not to complain with newer JS syntax
# CAUTION: npm is an old version: 3.5.2
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get update && apt-get install -y --no-install-recommends \
        nodejs \
        npm \
        git-all

# Git clone the app code and npm install dependencies
WORKDIR "/mycity"
RUN git clone https://github.com/Setogit/cityline.git \
    && cd cityline \
    && npm install

# Still need to bind in runtime like "-p 80:3000"
EXPOSE 3000

WORKDIR "/mycity"
CMD ["nodejs", "--use_strict", "cityline/index.js"]
