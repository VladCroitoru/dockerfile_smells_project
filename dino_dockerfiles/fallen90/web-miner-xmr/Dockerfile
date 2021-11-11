FROM node:8.6

WORKDIR /app
COPY . .

RUN apt-get update \
  && apt-get install -y \
      libpangocairo-1.0-0 \
      libx11-xcb1 \
      libxcursor1 \
      libxdamage1 \
      libxi6 \
      libxtst6 \
      libnss3 \
      libcups2 \
      libxss1 \
      libxrandr2 \
      libgconf2-4 \
      libasound2 \
      libatk1.0-0 \
      libgtk-3-common \
  && apt-get autoremove -y \
  && yarn global add puppeteer \
  && yarn cache clean \
  && rm -Rf /tmp/* /var/lib/apt/lists/* \
  && yarn \
  && cd coin-hive \
  && yarn \
  && cd /app

ENV NODE_PATH /usr/local/share/.config/yarn/global/node_modules

EXPOSE 80
CMD ["npm", "start"]