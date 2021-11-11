# First image to compile typescript to javascript
FROM node:16.5.0-alpine AS build-image
WORKDIR /app
COPY . .
RUN npm ci
RUN npm run clean
RUN npm run build

# Second image, that creates an image for production
FROM node:16.5.0-alpine AS prod-image
WORKDIR /app
COPY --from=build-image ./app/dist ./dist
COPY package* ./
RUN npm ci --production
CMD [ "node", "./dist/src/index.js" ]