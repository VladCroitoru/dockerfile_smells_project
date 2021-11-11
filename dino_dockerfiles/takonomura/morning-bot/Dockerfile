FROM node:8.9.1-slim

RUN apt-get update && apt-get install -y wget unzip --no-install-recommends \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-unstable --no-install-recommends \
    && mkdir -p /tmp/noto \
    && wget -q -O /tmp/noto/NotoSansCJKjp-hinted.zip https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip \
    && unzip -d /tmp/noto /tmp/noto/NotoSansCJKjp-hinted.zip \
    && mkdir -p /usr/share/fonts/noto \
    && cp /tmp/noto/*.otf /usr/share/fonts/noto \
    && chmod 644 /usr/share/fonts/noto/*.otf \
    && fc-cache -fv \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge --auto-remove -y curl unzip \
    && rm -rf /src/*.deb

COPY . /app/
WORKDIR /app

RUN groupadd -r pptruser && useradd -r -g pptruser -G audio,video pptruser \
    && mkdir -p /home/pptruser/Downloads \
    && chown -R pptruser:pptruser /home/pptruser \
    && chown -R pptruser:pptruser /app
USER pptruser

RUN yarn

CMD ["node", "src/index.js"]
