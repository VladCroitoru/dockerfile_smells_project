FROM node:alpine As development

WORKDIR /app

COPY package*.json ./

RUN npm install --only=development

COPY . .

RUN npm run build

FROM node:alpine as production

ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

WORKDIR /app

COPY package*.json ./

RUN npm install --only=production

COPY --from=development /app/dist ./dist

COPY env.txt ./.env

CMD ["node", "/app/dist/src/main"]