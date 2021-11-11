FROM node:14.15.4-stretch-slim as build
WORKDIR /app
COPY package*.json ./
RUN npm install --only=production
COPY .babelrc.* ./
COPY webpack.config.js webpack.config.js
COPY src/ src/
RUN npm install
COPY . .
RUN npm run build
RUN npm rebuild node-sass

FROM node:14.15.4-stretch-slim
WORKDIR /app
COPY --from=build /app/dist dist
COPY package* ./
RUN npm i --production
RUN chown -R node /app
ENV NODE_ENV=production
USER node
EXPOSE 7001
CMD ["npm","start"]