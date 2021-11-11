FROM node:carbon

WORKDIR /app

COPY . /app

RUN npm i \
 && npm run build \
 && npm prune --production \
 && rm -rf src *.json

CMD ["node", "dist/main.js"]
