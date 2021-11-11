FROM node:7 AS node
FROM php:7.4-fpm

# init env varioubles
ENV NODE_ENV=prod
ENV CONFIG_BASEDIR=/configs
ENV CONFIG_DIR=site-image

COPY --from=node /usr/local/lib/node_modules /usr/local/lib/node_modules
COPY --from=node /usr/local/bin/node /usr/local/bin/node

RUN ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm

RUN sed -i 's#http://deb.debian.org#http://mirrors.cloud.tencent.com#g' /etc/apt/sources.list

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends supervisor curl redis-server nginx git unzip

# update configuration of nginx using "daemon off" mode
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# init root directory

COPY resume/markdown-resume/composer.lock /app/resume/markdown-resume/composer.lock
COPY resume/markdown-resume/composer.json /app/resume/markdown-resume/composer.json
RUN cd /app/resume/markdown-resume && php -r "copy('https://install.phpcomposer.com/installer', 'composer-setup.php');" && php composer-setup.php
RUN cd /app/resume/markdown-resume && php composer.phar config -g repo.packagist composer https://packagist.phpcomposer.com && php composer.phar install --no-dev --no-interaction

COPY image/package-lock.json /app/image/package-lock.json
COPY image/package.json /app/image/package.json
RUN cd /app/image && npm install --registry https://registry.npm.taobao.org

# init nginx
COPY ./dockerfiles/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./dockerfiles/xhinliang.com.conf /etc/nginx/sites-enable/default
COPY ./dockerfiles/xhinliang.com.conf /etc/nginx/sites-available/default
COPY ./dockerfiles/redis.conf /etc/redis/redis.conf

ADD . /app
RUN cd /app/resume/ && ./markdown-resume/bin/md2resume html en.md /app/resume/ --title "XhinLiang's CV" && cp /app/resume/en.html /app/resume/index.html
RUN cd /app/resume/ && ./markdown-resume/bin/md2resume html cn.md /app/resume/ --title "XhinLiang's CV"
RUN cd /app/resume/ && ./markdown-resume/bin/md2resume html en-enhanced.md /app/resume/ --title "XhinLiang's CV"
RUN cd /app/resume/ && ./markdown-resume/bin/md2resume html cn-enhanced.md /app/resume/ --title "XhinLiang's CV"
# run supervisor
CMD ["/usr/bin/supervisord"]
EXPOSE 2333
