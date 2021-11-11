FROM node:boron-slim

ENV QBITTORRENT_USERNAME 'admin'
ENV QBITTORRENT_PASSWORD 'password'
ENV QBITTORRENT_HOST '127.0.0.1'
ENV QBITTORRENT_PORT '8080'
ENV DOWNLOAD_DIR '/downloads/tv_shows'
ENV FEED_URL ''

COPY qbittorrent-rss-downloader.coffee /usr/src/qbittorrent-rss-downloader/

COPY package.json /usr/src/qbittorrent-rss-downloader/

WORKDIR /usr/src/qbittorrent-rss-downloader/

RUN npm install -g coffee-script && npm install

CMD ["coffee","qbittorrent-rss-downloader.coffee"]
