FROM debian:wheezy-slim

RUN apt-get update

RUN apt-get install -y curl

RUN curl https://nodejs.org/dist/v8.11.2/node-v8.11.2-linux-x64.tar.xz --output node.tar.xz
RUN tar -xf node.tar.xz

RUN ln -s /node-v8.11.2-linux-x64/bin/node /usr/local/bin/node
RUN ln -s /node-v8.11.2-linux-x64/bin/npm /usr/local/bin/npm

RUN npm install --global coffeescript
RUN ln -s /node-v8.11.2-linux-x64/bin/coffee /usr/local/bin/coffee

RUN npm install --global babel-cli
RUN ln -s /node-v8.11.2-linux-x64/bin/babel /usr/local/bin/babel


CMD cd /assets && coffee -o js/ -cw coffee/
