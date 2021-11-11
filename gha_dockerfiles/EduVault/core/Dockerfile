FROM node:12-alpine AS build-stage
ENV PATH /eduvault/node_modules/.bin:/eduvault/api/node_modules/.bin:/eduvault/app/node_modules/.bin:$PATH

WORKDIR /eduvault/
COPY package*.json ./
RUN npm ci --production

WORKDIR /eduvault/api
COPY ./api/package*.json ./
RUN npm ci

WORKDIR /eduvault/app
COPY ./app/package*.json ./
RUN npm ci

WORKDIR /eduvault/
COPY . .

FROM build-stage AS prod-stage

WORKDIR /eduvault/
RUN npm run build:api
RUN npm run build:app
CMD ["npm", "run", "start"]
