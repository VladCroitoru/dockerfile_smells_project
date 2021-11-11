FROM node:lts-alpine as builder

WORKDIR /opt/app

COPY . .

RUN npm install; npm run build

FROM node:lts-alpine

### turn production mode on
ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

WORKDIR /opt/app

### copy app files
COPY --from=builder /opt/app/dist ./dist
COPY --from=builder /opt/app/node_modules ./node_modules

COPY --from=builder /opt/app/templates ./templates

CMD ["node", "dist/main"]