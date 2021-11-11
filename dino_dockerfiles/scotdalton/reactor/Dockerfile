FROM node:8.1-alpine

ENV APP_DIR   /var/www
ENV PATH      ${APP_DIR}/node_modules/.bin:${PATH}
WORKDIR       ${APP_DIR}
COPY          /package.json ${APP_DIR}/
RUN           npm install
COPY          /src ${APP_DIR}/src
COPY          /koa.coffee ${APP_DIR}/
COPY          /Gulpfile.coffee ${APP_DIR}/
RUN           gulp
CMD           npm start
