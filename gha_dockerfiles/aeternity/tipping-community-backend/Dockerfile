FROM node:lts-alpine

# Installs latest Chromium package.
RUN apk update && apk upgrade && apk add --no-cache \
      build-base \
      python3 \
      chromium \
      nss \
      freetype \
      harfbuzz \
      ca-certificates \
      ttf-freefont \
      git

# Tell Puppeteer to skip installing Chrome. We'll be using the installed package.
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true

# Add user so we don't need --no-sandbox.
RUN addgroup -S pptruser && adduser --uid 1001 -S -g pptruser pptruser \
    && mkdir -p /home/pptruser/Downloads /app \
    && chown -R pptruser:pptruser /home/pptruser \
    && chown -R pptruser:pptruser /app

WORKDIR /app
COPY package.json /app
COPY package-lock.json /app
RUN npm ci

# Do some cleanup
RUN apk del --no-cache \
      build-base \
      python3 \
      git

COPY . /app

RUN npm run swagger:create

RUN chown -R pptruser:pptruser /app

# Run everything after as non-privileged user.
USER pptruser

# Create swagger file

EXPOSE 3000

CMD npm run db:create; node bin/www
