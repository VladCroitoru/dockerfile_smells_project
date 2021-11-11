FROM node:0.12-onbuild
RUN npm install -g gulp knex && npm install pg
RUN NODE_ENV=production gulp
ENV NODE_ENV docker
CMD knex migrate:latest --env config && npm start
EXPOSE 3000
