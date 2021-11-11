FROM mhart/alpine-node

ADD . /src

WORKDIR /src

RUN npm install

EXPOSE  8080

ENV NODE_ENV development

CMD ["node", "index.js"]
