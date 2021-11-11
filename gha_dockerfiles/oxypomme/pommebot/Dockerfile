FROM node:16.6.0-alpine

# Tell Puppeteer to skip installing Chrome. We'll be using the installed package.
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
  PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser \
  NODE_ENV=production

WORKDIR /app

COPY . ./

# Upgrade
RUN apk update \
  && apk upgrade -U -a \
  # Install Puppeteer
  && apk add --no-cache chromium nss freetype harfbuzz ca-certificates ttf-freefont \
  # Install dependecies
  && yarn --prod

# Add user so we don't need --no-sandbox.
RUN addgroup -S pptruser && adduser -S -g pptruser pptruser \
  && mkdir -p /home/pptruser/Downloads \
  && chown -R pptruser:pptruser /home/pptruser \
  && chown -R pptruser:pptruser /app

# Run everything after as non-privileged user.
USER pptruser

CMD yarn start:prod

EXPOSE 8080
