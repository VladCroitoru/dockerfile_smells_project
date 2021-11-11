FROM node:14

# Create app directory
WORKDIR /usr/src/app

COPY package*.json ./

RUN npm ci

COPY next.config.js next.config.js
COPY next-env.d.ts next-env.d.ts
COPY tsconfig.json tsconfig.json
COPY public public
COPY src src
COPY store store
COPY types types

EXPOSE 1-65535

CMD [ "bash", "-c", "npm run build && npm run start" ]