FROM node:16.9.1-alpine as base

WORKDIR /app

#########################################
FROM base as backend

COPY --chown=node:node package.json ./
COPY --chown=node:node package-lock.json ./

RUN apk --update-cache add build-base libtool autoconf automake python2 sudo && \
    chown -R node:node /app/ && \
    sudo -u node npm install && \
    apk del build-base libtool autoconf automake python2

COPY --chown=node:node . .

#########################################
FROM backend as frontend

WORKDIR /app/src/frontend

RUN npm install
RUN npm run build

#########################################
FROM backend
COPY --from=frontend /app/src/frontend/build/ ./src/frontend/build/

USER root
RUN apk --update-cache add ffmpeg

ENV NODE_ENV=production

USER node 
RUN npm run build

# start app
CMD ["node", "dist/backend/app.js"]