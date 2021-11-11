FROM node:7.4.0-alpine

ENV ROOTPATH /Manga
EXPOSE 8080
VOLUME /Manga

COPY build package.json /home/MangaReader/
RUN cd /home/MangaReader && npm install

ENTRYPOINT node /home/MangaReader/index.js
