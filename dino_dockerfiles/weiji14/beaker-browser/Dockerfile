FROM debian:buster-slim
LABEL maintainer "https://github.com/weiji14"
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Install standard dependencies a la buildpack-deps curl https://hub.docker.com/_/buildpack-deps/
RUN apt-get -qq update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

ENV NODE_VERSION=8

# Get node source as per https://github.com/nodesource/distributions#installation-instructions
# Install npm and update it to the latest version
RUN curl -sL https://deb.nodesource.com/setup_$NODE_VERSION.x | bash - \
    && apt-get -qq update \
    && apt-get install -y --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*

# Get beaker browser source files and dependencies https://github.com/beakerbrowser/beaker#building-from-source
RUN apt-get -qq update && apt-get install -y --no-install-recommends \
    libtool \
    m4 \
    automake \
    make \
    g++ \
    git \
    libgtk2.0-0 \
    libx11-xcb1 \
    libxtst6 \
    libxss1 \
    libgconf-2-4 \
    libnss3 \
    libasound2 \
    python

# Setup beaker user and workdir
RUN useradd -d /home/beaker -m beaker
USER beaker
WORKDIR /home/beaker

# Git clone from beaker's github source and use latest tagged release
RUN git clone https://github.com/beakerbrowser/beaker.git
WORKDIR /home/beaker/beaker
RUN git checkout `git tag | sort -n | tail -1`
#RUN git checkout `git for-each-ref --sort='*authordate' --format='%(tag)' refs/tags | tail -1`  #see https://stackoverflow.com/a/2818692/6611055

# Build and install beaker browser using npm
RUN npm install && npm run burnthemall
#RUN npm run rebuild #see https://github.com/electron/electron/issues/5851
EXPOSE 80
CMD ["npm", "start"]
