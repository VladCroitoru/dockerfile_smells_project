FROM ubuntu:latest
# Install Utilities
RUN apt-get update -q \
    && apt-get install -yqq \
    apt-utils \
    cron \
    curl \
    vim \
    sudo \
    make \
    gcc \
    libkrb5-dev \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Install nodejs
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN apt-get install -yq nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


ENV NODE_ENV=production
ENV HOST 0.0.0.0


# Create app directory dor docker
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
# RUN apt update && apt upgrade && apt add git

COPY . /usr/src/app/
RUN npm install

# Build app
RUN npm run build

EXPOSE 3000
CMD [ "npm", "start" ]
