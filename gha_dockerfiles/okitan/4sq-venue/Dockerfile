from alekzonder/puppeteer:latest

# WORKDIR of alekzonder/puppeteer
ENV APP_ROOT  /app
ENV LANG      ja_JP.UTF-8

COPY package.json       $APP_ROOT
COPY package-lock.json  $APP_ROOT

RUN \
  npm install

COPY --chown=pptruser:pptruser . $APP_ROOT

# but seems not working
CMD ["node", "lib/cli.js", "--help"]
