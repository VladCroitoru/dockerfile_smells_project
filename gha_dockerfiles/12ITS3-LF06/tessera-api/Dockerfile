FROM node:14-alpine as build
WORKDIR /opt/app
COPY package* ./
RUN npm ci --verbose
COPY . .
RUN npm run build

FROM node:14-alpine
WORKDIR /opt/app
COPY package* ./
RUN npm ci --verbose --production
COPY --from=build /opt/app/dist ./dist
CMD npm run start:prod
