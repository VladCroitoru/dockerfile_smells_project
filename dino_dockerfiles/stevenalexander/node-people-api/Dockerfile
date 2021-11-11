FROM node:8.11.3-alpine

RUN mkdir -p /usr/src/app/app
RUN mkdir -p /usr/src/app/migrations
WORKDIR /usr/src/app

COPY ["package.json", "package-lock.json", "knexfile.js", "wait-for-postgres.sh", "/usr/src/app/"]
COPY app /usr/src/app/app
COPY migrations /usr/src/app/migrations
RUN export NODE_ENV=production
RUN npm install --only=production

EXPOSE 3001

HEALTHCHECK CMD curl --fail http://localhost:3001/people/status || exit 1

CMD ./wait-for-postgres.sh && node_modules/.bin/knex migrate:latest --env development && npm start