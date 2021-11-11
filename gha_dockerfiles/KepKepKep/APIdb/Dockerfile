FROM node:16-alpine

WORKDIR /api

COPY . .

RUN npm install
RUN npm run tsc &

EXPOSE 8080/tcp

CMD ["node", "./build/index.js"]
