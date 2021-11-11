FROM node:14.17-slim

WORKDIR /usr/local/app

COPY package*.json ./

RUN npm install

COPY ./ ./

ENV NODE_ENV=production

RUN npm run build

ENTRYPOINT ["./scripts/entrypoint.sh"] 
