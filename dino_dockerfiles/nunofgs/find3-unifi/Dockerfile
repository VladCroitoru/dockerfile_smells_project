FROM node:alpine

WORKDIR /home/node

COPY package.json package-lock.json ./

RUN npm install

COPY . ./

USER node

ENTRYPOINT ["node"]

CMD ["src/index.js"]
