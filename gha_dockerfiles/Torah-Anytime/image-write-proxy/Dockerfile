FROM node:14-alpine as builder
WORKDIR /app

COPY . ./
RUN npm install
RUN npm run build

FROM node:14-alpine as runner
WORKDIR /app

COPY --from=builder ./app/dist ./dist
COPY . ./
RUN npm install --production

ENTRYPOINT [ "npm", "start" ]