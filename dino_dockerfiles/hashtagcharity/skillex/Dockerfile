FROM node:0.10-wheezy

ENV PORT 3000

EXPOSE 3000

ADD . /skillex

WORKDIR /skillex

RUN npm install

CMD ["node", "index.js"]
