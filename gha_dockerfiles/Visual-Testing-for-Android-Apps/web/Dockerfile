FROM node:14-alpine AS BUILD_STAGE

# working directory
WORKDIR /usr/src/app

# copy all dependencies
COPY package*.json ./

RUN npm ci --only=production

# Bundle app source
COPY . .

FROM gcr.io/distroless/nodejs:14

COPY --from=BUILD_STAGE /usr/src/app /app

WORKDIR /app

EXPOSE 3000

CMD ["server.js"]
