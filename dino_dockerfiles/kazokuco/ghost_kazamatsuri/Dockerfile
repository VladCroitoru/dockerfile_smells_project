FROM node:4-slim
RUN apt-get -qq update && apt-get -qq -y install git && apt-get clean
RUN npm install -q -g bower broccoli-cli && npm -q cache clean
WORKDIR /data
ADD . .
RUN npm -q install && bower --allow-root install && broccoli build assets
