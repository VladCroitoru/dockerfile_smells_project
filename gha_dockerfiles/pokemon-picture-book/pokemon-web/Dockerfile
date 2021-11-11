# ビルド環境
FROM node:16 as build-stage
WORKDIR /usr/app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# 本番環境
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /usr/app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]