# ビルド環境
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
COPY patches/ /app/patches/
RUN npm ci --only=production --unsafe-perm
COPY . .
RUN npm run build

# 本番環境
FROM pierrezemb/gostatic as production-stage
COPY --from=build-stage /app/dist /srv/http
CMD ["-port", "8080", "-fallback", "index.html"]
