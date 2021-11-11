# This Dockerfile uses multi-stage builds as recommended in
# https://github.com/nodejs/docker-node/blob/master/docs/BestPractices.md
#
FROM node:14 AS frontend
WORKDIR /usr/src/app/frontend

COPY ["frontend/package.json", "package.json"]
COPY ["frontend/package-lock.json", "package-lock.json"]

# See: https://stackoverflow.com/questions/18136746/npm-install-failed-with-cannot-run-in-wd
RUN npm ci --unsafe-perm
COPY frontend .
RUN npm run build

FROM node:14 AS backend
WORKDIR /usr/src/app/backend

COPY ["backend/package.json", "package.json"]
COPY ["backend/package-lock.json", "package-lock.json"]

RUN npm ci --production --unsafe-perm

FROM node:14-alpine AS production
WORKDIR /usr/src/app
COPY --from=frontend /usr/src/app/frontend/build frontend/build
COPY --from=backend /usr/src/app/backend/node_modules backend/node_modules
COPY . .

EXPOSE 4000

CMD cd backend && node app.js
