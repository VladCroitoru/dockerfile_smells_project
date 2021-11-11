FROM node:8

WORKDIR /opt/makerscraper

VOLUME /opt/makerscraper_config

COPY package.json package-lock.json tsconfig.json /opt/makerscraper/
COPY src /opt/makerscraper/src/
COPY config/default.js /opt/makerscraper/config/

RUN groupadd -g 1001 scraper && \
  useradd -u 1001 -g 1001 scraper && \
  mkdir -p /opt/makerscraper_config /opt/makerscraper/config && \
  ln -sf /opt/makerscraper_config/app.js /opt/makerscraper/config/production.js && \
  npm install && \
  npm run build && \
  npm prune --production

USER scraper:scraper
ENV NODE_ENV=production
CMD ["/usr/local/bin/node", "/opt/makerscraper/dist/index.js"]
