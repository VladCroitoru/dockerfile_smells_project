FROM node:alpine as builder
WORKDIR '/app'
COPY ./package.json ./
RUN npm install 
COPY . . 
RUN npm run build:develop

FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html

EXPOSE 80 