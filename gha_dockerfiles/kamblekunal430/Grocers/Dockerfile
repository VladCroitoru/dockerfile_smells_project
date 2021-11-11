FROM node:lts-alpine as Client
WORKDIR /client
COPY client/package*.json /
RUN npm install
COPY client/ ./
RUN npm run build



FROM node:lts-alpine
WORKDIR /server

COPY --from=Client /client/build/ ./client/build/

COPY server/package*.json ./
RUN npm install
COPY server/ ./
EXPOSE 8000
CMD ["npm", "start"]