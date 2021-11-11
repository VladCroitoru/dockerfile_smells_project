FROM node:alpine as build
WORKDIR /usr/src/app
COPY package*.json ./
COPY tsconfig.json ./
RUN npm install
COPY . . 
RUN npm run build

FROM node:alpine
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install --production
COPY *.env ./
COPY --from=build /usr/src/app/dist ./dist
CMD ["npm", "run", "start:production"]