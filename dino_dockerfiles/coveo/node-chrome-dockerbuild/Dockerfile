FROM node:12-buster

# Ensure we use the latest version of npm.
RUN npm i -g npm

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'

RUN apt-get update
RUN apt-get install -y jq
RUN apt-get install -y python
RUN apt-get install -y google-chrome-stable

RUN apt-get install -yq libgconf-2-4
RUN apt-get install -y make build-essential libssl-dev zlib1g-dev   
RUN apt-get install -y libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm 
RUN apt-get install -y libncurses5-dev  libncursesw5-dev xz-utils tk-dev

RUN apt-get install -y openjdk-11-jdk

RUN echo "[hostsecurity]\nminimunprotocol = tls1.2" > etc/mercurial/hgrc