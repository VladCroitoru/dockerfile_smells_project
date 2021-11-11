FROM debian
MAINTAINER Ryan Grieve <ryan@rehabstudio.com>

# update, upgrade and install base requisites
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        apt-transport-https \
        inotify-tools \
        build-essential \
        sudo \
        git \
        wget \
        curl

# install node from ppa
RUN curl -sL https://deb.nodesource.com/setup | bash -
RUN apt-get install -y nodejs

RUN apt-get install -y unzip

# Install Ghost
RUN \
  cd /tmp && \
  wget https://ghost.org/zip/ghost-latest.zip && \
  unzip ghost-latest.zip -d /ghost && \
  rm -f ghost-latest.zip && \
  cd /ghost && \
  npm install --production && \
  sed 's/127.0.0.1/0.0.0.0/' /ghost/config.example.js > /ghost/config.js && \
  useradd ghost --home /ghost

# Add files.
ADD start.bash /ghost-start

# Set environment variables.
ENV NODE_ENV production

# Define mountable directories.
VOLUME ["/data", "/ghost-override"]

# Define working directory.
WORKDIR /ghost

# Define default command.
CMD ["bash", "/ghost-start"]

# Expose ports.
EXPOSE 2368
