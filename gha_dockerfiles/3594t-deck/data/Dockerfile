FROM node:14-slim AS chrome

ENV LANG=C.UTF-8 TZ=Asia/Tokyo

RUN apt-get update \
    && apt-get install -y wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1 git \
      --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/google-chrome-stable PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true

ARG WORKDIR

RUN mkdir -p $WORKDIR

WORKDIR $WORKDIR

FROM chrome AS crawler

ARG WORKDIR

COPY ./ $WORKDIR

RUN mkdir -p "$WORKDIR/data"

RUN npm --production=false install \
    && npm run build

VOLUME ["$WORKDIR/data"]

CMD ["npm", "start"]
