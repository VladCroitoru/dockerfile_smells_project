FROM alpine:latest

# Install required packages
RUN apk add --no-cache \
      chromium \
      nss \
      freetype \
      harfbuzz \
      ca-certificates \
      ttf-freefont \
      nodejs \
      yarn

# Set up Puppeter
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser
ENV PATH="/usr/src/app:${PATH}"

ENTRYPOINT ["/bin/sh"]