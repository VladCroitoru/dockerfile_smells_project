FROM node:alpine as builder
RUN mkdir -p /app
WORKDIR /app

COPY ./package*.json ./
RUN npm install --prefer-online


COPY ./ ./

RUN npm run build


FROM nginx:1.20.1-alpine

COPY --from=builder /app/build /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]