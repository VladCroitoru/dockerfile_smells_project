FROM node:14-alpine as builder

WORKDIR /usr/src/app
COPY . .
RUN npm ci
RUN npm run build


FROM node:14-alpine as runner

ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}
ENV PORT=8080

WORKDIR /usr/src/app
COPY package*.json ./
RUN npm i --only=production

COPY --from=builder /usr/src/app/dist ./dist

CMD ["node", "dist/main"]

