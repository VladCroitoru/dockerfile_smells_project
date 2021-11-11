FROM node:14-slim

# Install utilities and libraries
RUN apt-get update && apt-get install -y ca-certificates gnupg2 wget \
    libxtst6 libxss1 \
    --no-install-recommends

# Install latest chrome package.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf \
    --no-install-recommends

# Clean our room
RUN rm -rf /var/lib/apt/lists/*

RUN yarn add express@4.17.1 \
    && yarn add sharp@0.27.1 \
    && yarn add puppeteer@7.1.0 \
    && groupadd -r pptruser && useradd -r -g pptruser -G audio,video pptruser \
    && mkdir -p /home/pptruser/Downloads \
    && chown -R pptruser:pptruser /home/pptruser \
    && chown -R pptruser:pptruser /node_modules

RUN yarn cache clean

HEALTHCHECK --interval=120s --timeout=15s --start-period=60s \
    CMD node /docker_healthcheck.js

COPY screenshotr.js /screenshotr.js
COPY pdfr.js /pdfr.js
COPY browser.js /browser.js
COPY docker_healthcheck.js /docker_healthcheck.js
COPY healthcheck.js /healthcheck.js
COPY app.js /app.js

RUN chmod +x /app.js \
    && chmod +x /docker_healthcheck.js

USER pptruser

EXPOSE 3000
CMD ["/app.js"]