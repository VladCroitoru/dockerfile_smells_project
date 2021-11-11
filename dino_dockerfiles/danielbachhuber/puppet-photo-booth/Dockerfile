FROM node:8

# Install Chrome dependencies
RUN apt-get update && apt-get install -y wget --no-install-recommends \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-unstable \
      --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge --auto-remove -y curl \
    && rm -rf /src/*.deb

# Install ImageMagick
RUN apt-get install -y imagemagick libmagickcore-dev libmagickwand-dev --no-install-recommends && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY package.json .
COPY yarn.lock .

RUN npm install -g yarn
RUN yarn install

# Bundle app source
COPY . .

ENV PPB_LAUNCH_CHROME_INSECURE 1

EXPOSE 8080
CMD [ "npm", "start" ]
