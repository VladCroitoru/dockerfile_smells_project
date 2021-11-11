FROM node:17-alpine as development

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install --only=development

COPY . .

RUN npm run build

FROM node:17-alpine as production

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install --only=production

COPY . .

COPY --from=development /usr/src/app/dist ./dist

ARG PORT=4413
ENV PORT=${PORT}
ARG IP="0.0.0.0"
ENV IP=${IP}

LABEL authors="greatSumini@gmail.com"

CMD [ "node", "dist/main" ]
