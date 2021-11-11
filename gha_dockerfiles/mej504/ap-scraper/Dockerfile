FROM node:alpine

RUN mkdir /app
RUN npm install -g pm2

WORKDIR /app

COPY package.json /app
COPY package-lock.json /app

RUN npm install --production
COPY . /app

RUN npm run build

ENV PORT=4010
ENV NODE_ENV=production
ENV INLINE_RUNTIME_CHUNK=false
ENV PUBLIC_URL=/NewsScraper

EXPOSE 4010

USER node

CMD ["pm2-runtime", "./bin/init.js"]
