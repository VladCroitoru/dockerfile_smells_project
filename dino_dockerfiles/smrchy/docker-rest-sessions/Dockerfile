FROM node:12.18.3-alpine
RUN mkdir /src

WORKDIR /src
RUN npm install rest-sessions@2.0.1 --production

EXPOSE 3000

CMD ["node", "/src/node_modules/rest-sessions/server.js", "--max-old-space-size=32"]
