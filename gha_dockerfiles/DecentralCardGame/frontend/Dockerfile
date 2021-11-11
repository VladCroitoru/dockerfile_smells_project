# build stage
FROM node:lts as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN bash bin/postinstall.sh
RUN npm run build

# production stage
FROM nginx as production-stage
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
