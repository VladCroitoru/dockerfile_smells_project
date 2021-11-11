FROM node:12-slim

RUN apt-get update \
    && apt-get install -y wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1 \
      --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY . ./ofertas-3dgames-notifier/

WORKDIR /ofertas-3dgames-notifier/

RUN npm install

ARG TELEGRAM_BOT_TOKEN
ENV TELEGRAM_BOT_TOKEN=$TELEGRAM_BOT_TOKEN

ARG TELEGRAM_CHANNEL
ENV TELEGRAM_CHANNEL=$TELEGRAM_CHANNEL

ARG PGHOST
ENV PGHOST=$PGHOST

ARG PGDATABASE
ENV PGDATABASE=$PGDATABASE

ARG PGPASSWORD
ENV PGPASSWORD=$PGPASSWORD

ARG PGUSER
ENV PGUSER=$PGUSER

CMD npm run start
