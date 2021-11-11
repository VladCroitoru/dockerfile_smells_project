FROM node
MAINTAINER ZHANGZHANQI <zhangzhanqicixi@gmail.com>
WORKDIR /app
# install hexo
RUN npm install hexo-cli -g
RUN hexo init .
RUN npm install
# install apollo deploy
RUN npm install --save hexo-renderer-jade hexo-generator-feed hexo-generator-sitemap hexo-generator-archive
RUN npm install hexo-hide-posts --save
COPY _config.yml .
COPY ./source/ ./source/
COPY ./themes/apollo ./themes/apollo
CMD ["hexo", "s", "-l"]