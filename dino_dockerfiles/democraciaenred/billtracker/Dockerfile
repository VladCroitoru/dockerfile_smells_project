FROM node:8.11.3-alpine

WORKDIR /usr/src

COPY ["package.json", "package-lock.json", "/usr/src/"]

ARG NODE_ENV=production
ENV NODE_ENV=$NODE_ENV

# RUN BLUEBIRD_WARNINGS=0 npm ci --loglevel=error
RUN npm i --loglevel=warn --progress=false --porcelain

COPY [".", "/usr/src/"]

RUN npm run build

EXPOSE 3000

CMD ["node", "."]
