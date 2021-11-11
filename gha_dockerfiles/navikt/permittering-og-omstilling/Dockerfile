FROM node:14-alpine

WORKDIR /app
ENV NODE_ENV production

COPY .next ./.next
COPY public ./public
COPY package.json ./package.json
COPY next.config.js ./next.config.js

RUN yarn add next@11.1.2

RUN chown -R 1069:1069 /app/.next

CMD ["yarn", "start"]
