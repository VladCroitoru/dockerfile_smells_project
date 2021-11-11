FROM node:lts-alpine as build

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:lts-alpine

COPY --from=build /app/dist /app/dist
RUN npm install -g http-server
WORKDIR /app
EXPOSE 8080
CMD [ "http-server", "dist" ]
