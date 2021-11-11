FROM node:8.9.1-alpine

# アプリをビルド
RUN mkdir -p /use/src/tmp
WORKDIR /usr/src/temp
COPY ./ /usr/src/temp/

RUN npm install \
     && npm run build

EXPOSE 3000
CMD [ "npm", "run", "run:server" ]


