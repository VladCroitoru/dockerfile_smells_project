FROM sitespeedio/webbrowsers:firefox-54.0-chrome-60.0

USER root
RUN apt-get update && apt-get install -y curl

# Find your desired version here: https://deb.nodesource.com/node_8.x/pool/main/n/nodejs/
# Ubuntu 16.04.3 LTS (Xenial Xerus) (https://wiki.ubuntu.com/Releases)
RUN curl https://deb.nodesource.com/node_8.x/pool/main/n/nodejs/nodejs_8.2.1-2nodesource1~xenial1_amd64.deb > node.deb \
 && dpkg -i node.deb \
 && rm node.deb

RUN npm --global install grunt-cli