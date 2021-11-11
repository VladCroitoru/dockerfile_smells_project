FROM node:alpine as builder
RUN export NODE_OPTIONS="--max-old-space-size=8192"
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build


FROM nginx
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80
