FROM node:12

WORKDIR /usr/src/Pixel-Shelf

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y sqlite3

COPY package.json ./
COPY package-lock.json ./

RUN npm install

COPY . .

RUN npx node-sass --omit-source-map-url sass/styles.scss public/stylesheets/styles.css

RUN mkdir models/db
RUN cat models/initdb.sql | sqlite3 models/db/pixelshelf.db

RUN mkdir secrets

ENV PORT=3000
EXPOSE 3000

CMD [ "node", "bin/www" ]