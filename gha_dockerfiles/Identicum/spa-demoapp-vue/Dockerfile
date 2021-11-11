FROM node:12.14.1-alpine as build-stage
WORKDIR /app
COPY spa/package*.json ./
RUN npm install
COPY spa/ .
RUN npm run build

FROM identicum/ipax:latest
COPY --from=build-stage /app/dist /var/ipax/html
