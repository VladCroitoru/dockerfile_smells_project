FROM node:12-slim

# Install Font
RUN mkdir /noto \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    udev \
    unzip \
    fontconfig \
    ca-certificates \
    wget \
  && wget -q -O /noto/noto.zip https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip \
  && unzip -d /noto/fonts /noto/noto.zip \
  && mkdir -p /usr/share/fonts/noto \
  && cp /noto/fonts/*.otf /usr/share/fonts/noto \
  && chmod 644 -R /usr/share/fonts/noto/ \
  && fc-cache -fv \
  && rm -rf /noto \
  && apt-get --force-yes remove -y --purge \
    unzip \
    fontconfig \
    ca-certificates \
    wget \
  && apt-get autoremove -y \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# Dependencies package
# https://github.com/GoogleChrome/puppeteer/blob/master/docs/troubleshooting.md
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    gconf-service \
    libasound2 \
    libatk1.0-0 \
    libc6 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libexpat1 \
    libfontconfig1 \
    libgcc1 \
    libgconf-2-4 \
    libgdk-pixbuf2.0-0 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libstdc++6 \
    libx11-6 \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libxrender1 \
    libxss1 \
    libxtst6 \
    ca-certificates \
    fonts-liberation \
    libappindicator1 \
    libnss3 \
    lsb-release \
    xdg-utils \
    wget \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

WORKDIR /usr/src/app

COPY package.json .
COPY package-lock.json .

RUN npm install --production

COPY . .

CMD ["npm", "start"]
VOLUME /usr/src/app/screenshots
