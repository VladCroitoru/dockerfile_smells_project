FROM node:10.6-alpine

# To get the latest version this requires having run `npm install`, `npm run build` prior to building the container

COPY build /usr/src/wowanalyzer/discordbot/build/
COPY node_modules /usr/src/wowanalyzer/discordbot/node_modules/
COPY package.json /usr/src/wowanalyzer/discordbot/
WORKDIR /usr/src/wowanalyzer/discordbot/

ENV NODE_ENV=production
USER node
CMD ["npm", "run", "prod"]
