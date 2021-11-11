FROM node:12.12.0
MAINTAINER Owen Barton <owen.barton@civicactions.com>

# Drydock environment setup
LABEL exposed.command.single=pa11y-ci
ENV TARGET=http://web

# From https://github.com/GoogleChrome/puppeteer/blob/master/docs/troubleshooting.md#running-puppeteer-in-docker
# See https://crbug.com/795759
RUN apt-get update && apt-get install -yq libgconf-2-4
# Install latest chrome dev package and fonts to support major charsets (Chinese, Japanese, Arabic, Hebrew, Thai and a few others)
# Note: this installs the necessary libs to make the bundled version of Chromium that Puppeteer
# installs, work.
RUN apt-get update && apt-get install -y wget --no-install-recommends \
  && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
  && apt-get update \
  && apt-get install -y google-chrome-unstable fonts-liberation ca-certificates fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst ttf-freefont \
  --no-install-recommends \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get purge --auto-remove -y curl \
  && rm -rf /src/*.deb
# It's a good idea to use dumb-init to help prevent zombie chrome processes.
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 /usr/local/bin/dumb-init
RUN chmod +x /usr/local/bin/dumb-init

# Switch to node user to install packages, so ownership is correct.
USER node
WORKDIR /home/node
COPY package.json yarn.lock ./
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true
RUN yarn install --production --non-interactive && \
  yarn cache clean --force
COPY entrypoint.sh ./
ENV PATH="/home/node/node_modules/.bin:${PATH}"

# Install default/autotest configuration and mount
VOLUME ["/src"]
WORKDIR /src
COPY pa11yci.conf.js pages.txt /src/

# Switch back to root so our entrypoint can adjust the running UID/GID.
USER root
ENTRYPOINT ["/home/node/entrypoint.sh"]

