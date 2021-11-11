# 前端构建
FROM node:latest as build-frontend
WORKDIR /app
COPY web /app
RUN yarn install && yarn build


# 后端构建
FROM php:7.3-cli-alpine as build-backend
ENV COMPOSER_ALLOW_SUPERUSER=true
ENV APP_ENV=production
# 准备代码和 composer
WORKDIR /app
COPY . /app
COPY --from=composer /usr/bin/composer /usr/bin/composer
# 安装依赖、初始化数据库、构建缓存等
RUN set -eux; \
    composer install --ignore-platform-reqs; \
    composer reset-database; \
    composer build; \
    php artisan storage:link



FROM php:7.3-cli-alpine
# 基础配置: 配置时区
RUN set -eux; \
    apk add --no-cache --virtual .tz-deps tzdata; \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime; \
    echo "Asia/Shanghai" >  /etc/timezone; \
    date; \
    apk del .tz-deps
RUN docker-php-ext-install sockets
# 复制代码
WORKDIR /app
COPY --from=build-backend /app /app
COPY --from=build-frontend /app/dist /app/public/dashboard
# 启动开发 server
CMD ["/usr/local/bin/php", "artisan", "serve", "--host=0.0.0.0"]
