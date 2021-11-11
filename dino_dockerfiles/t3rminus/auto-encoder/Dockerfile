FROM node:current-buster-slim

# Configure user nobody to match unRAID's settings
RUN usermod -u 99 nobody && \
    usermod -g 100 nobody && \
    usermod -d /home nobody && \
    chown -R nobody:users /home

RUN sed -i "s# buster/updates main# buster/updates main contrib non-free#g" /etc/apt/sources.list
RUN sed -i "s# buster main# buster main contrib non-free#g" /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y handbrake-cli mediainfo unzip unrar

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV DOCKER=1
WORKDIR "/opt"
ADD ["main.js", "package.json", "package-lock.json", "/opt/"]
ADD ["lib", "/opt/lib"]

VOLUME /watch
VOLUME /extract
VOLUME /output
VOLUME /movies
VOLUME /tv
VOLUME /config

RUN ["npm", "install"]
USER nobody:users
ENTRYPOINT ["node", "main.js"]