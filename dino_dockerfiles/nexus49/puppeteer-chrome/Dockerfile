# The basis for this dockerfile is: https://github.com/GoogleChrome/puppeteer/blob/master/docs/troubleshooting.md
FROM node:9-alpine

# Installs latest Chromium (63) package.
RUN apk update && apk upgrade && \
    echo @edge http://nl.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories && \
    echo @edge http://nl.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories && \
    apk add --no-cache \
      chromium@edge \
      nss@edge

# Tell Puppeteer to skip installing Chrome. We'll be using the installed package.
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true

# Puppeteer v0.11.0 works with Chromium 63.
RUN yarn add puppeteer@0.13.0

# Add user so we don't need --no-sandbox.
# RUN addgroup -S pptruser && adduser -S -g pptruser pptruser \
#     && mkdir -p /home/pptruser/Downloads \
#     && chown -R pptruser:pptruser /home/pptruser \
#     && mkdir /home/pptruser/app \
#     && chown -R pptruser:pptruser /home/pptruser/app

# Run everything after as non-privileged user.
# USER pptruser