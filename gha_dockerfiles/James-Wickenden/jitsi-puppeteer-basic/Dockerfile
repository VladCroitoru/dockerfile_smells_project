# syntax=docker/dockerfile:1

FROM node:12-slim
WORKDIR /puppeteer

RUN apt-get update \
    && apt-get install -y wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1 \
      --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*
# inherits node base image to build off and installs deps

# RUN apt-get install -y ffmpeg
# install ffmpeg (CURRENTLY DISABLED!)

ENV NODE_ENV=production
# improves performance

COPY ["package.json", "package-lock.json*", "./"]
# copies from local into docker image
RUN npm ci
RUN chmod -R o+rwx node_modules/puppeteer/.local-chromium
# installs puppeteer, and gives it permissions to run chromium's binary

RUN npm install --production
# installs node dependencies

COPY . .
# moves files into image

CMD [ "npm", "run", "start" ]
# runs image
