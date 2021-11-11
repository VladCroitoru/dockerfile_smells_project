FROM node:16-alpine as builder

RUN apk add --no-cache git python3 build-base

WORKDIR /opt/build

COPY package.json package-lock.json* ./

RUN npm ci --production
# RUN npm install

FROM node:16-alpine

WORKDIR /opt/reporting-events-processor-svc

COPY --from=builder /opt/build/node_modules node_modules
COPY package*.json ./
COPY src src

CMD ["npm", "start"]
