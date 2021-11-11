FROM mhart/alpine-node:6

ADD . /src

WORKDIR /src

ENV HOME /src

EXPOSE 3000

RUN npm install -g yarn

RUN yarn install

CMD ["node", "/src/index.js"]
