FROM node:14-alpine AS build-stage

WORKDIR /usr/src/app
COPY package*.json ./
COPY . .
RUN npm install
RUN npm run build

## this is stage two , where the app actually runs

FROM node:14-alpine
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install --only=production
COPY --from=build-stage /usr/src/app/dist ./
RUN ls
ENV NODE_ENV production
USER node
EXPOSE 3000
CMD ["node", "index.js"]