FROM node:13.14
WORKDIR /usr/src
COPY package.json package-lock.json /usr/src/
RUN npm i --production
COPY . .

FROM node:13.14-slim
WORKDIR /usr/src
COPY --from=0 /usr/src .
COPY . .
EXPOSE 8000
CMD ["node", "server.js"]
