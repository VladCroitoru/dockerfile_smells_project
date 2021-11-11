FROM zenato/puppeteer

USER root

RUN set -ex \
  && apt-get update \
  && apt-get install -y --no-install-recommends unzip \
  && mkdir -p /usr/share/fonts/opentype/noto \
  && wget https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKsc-hinted.zip -O /tmp/font.zip \
  && unzip /tmp/font.zip -d /usr/share/fonts/opentype/noto \
  && rm /tmp/font.zip \
  && apt-get purge --auto-remove -y unzip \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY . /app

WORKDIR /app
RUN yarn --no-progress

EXPOSE 3000
CMD yarn start
