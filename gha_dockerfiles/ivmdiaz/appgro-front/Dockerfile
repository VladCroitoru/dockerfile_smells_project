# Stage 1
FROM node:14.16.1-alpine as build-step
RUN mkdir -p /app
WORKDIR /app
COPY package.json /app
RUN npm install
COPY . /app
RUN npm run build

# Stage 2
FROM nginx
COPY --from=build-step /app/dist/fronted /usr/share/nginx/html
