FROM node:7.4-alpine

WORKDIR /app
EXPOSE 3000

COPY package.json /app
RUN npm install

COPY ./ /app/

CMD ["node", "index.js"]
