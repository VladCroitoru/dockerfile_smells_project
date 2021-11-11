FROM node:14-alpine AS build
WORKDIR /app
COPY package.json package-lock.json /app/
RUN npm ci --also=dev
COPY . /app/
RUN npx tsc

FROM node:14-alpine
WORKDIR /app
ENV NODE_ENV=production
COPY package.json package-lock.json /app/
RUN npm ci --production
COPY --from=build /app/build /app/
COPY src/assets/ /app/src/assets/
CMD ["node", "./src/server.js"]