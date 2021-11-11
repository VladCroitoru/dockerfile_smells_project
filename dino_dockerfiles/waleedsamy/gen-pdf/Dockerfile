FROM node:7

WORKDIR /src

ENV HOME /src

EXPOSE 3000

CMD ["node", "/src/index.js"]

ADD . /src

RUN npm install
RUN npm rebuild phantomjs-prebuilt
