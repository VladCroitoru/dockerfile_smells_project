FROM node:9.2
EXPOSE 3000
ADD release /release

ENV root_dir /release/www

RUN cd release && npm install

CMD  ["node", "/release/server/index.js"]