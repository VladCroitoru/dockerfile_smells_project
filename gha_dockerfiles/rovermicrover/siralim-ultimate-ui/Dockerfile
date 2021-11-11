FROM node:16-alpine as build

WORKDIR /ui

COPY package.json ./
COPY package-lock.json ./

RUN npm ci

COPY ./ ./

ENV NODE_ENV=production

RUN npm run build

FROM node:16-alpine
WORKDIR /ui
COPY --from=build /ui/build /ui/build

COPY package.json ./
COPY package-lock.json ./

RUN npm ci --only=production

EXPOSE 3000

CMD ["npm", "run",  "serve"]