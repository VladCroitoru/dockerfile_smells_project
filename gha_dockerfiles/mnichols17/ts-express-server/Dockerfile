FROM node as builder
WORKDIR /usr/mrd
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node
WORKDIR /usr/mrd
COPY package*.json ./
RUN npm install --production

COPY --from=builder /usr/mrd ./dist

COPY ormconfig.js .
COPY .env .

ENV NODE_ENV production

EXPOSE 5000
CMD node dist/src/server.js

