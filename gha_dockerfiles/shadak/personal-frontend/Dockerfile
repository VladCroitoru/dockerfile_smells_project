FROM node:16-alpine as build

WORKDIR /app
COPY package.json .
RUN npm install --verbose
COPY . .
RUN npm run build

FROM nginx:1.19-alpine
COPY --from=build /app/public /usr/share/nginx/html
