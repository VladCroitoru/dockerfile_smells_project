FROM node:12-alpine AS runtime
RUN apk add --no-cache curl

WORKDIR /app
ENV NODE_ENV=production
EXPOSE 5000

COPY package.json yarn.lock /app/
RUN yarn install --production --pure-lockfile

COPY dist /app/dist
COPY static /app/static
COPY views /app/views
COPY public /app/public
COPY .env.example /app/.env.example
RUN touch /app/.env

USER node
CMD ["node", "dist/index.js"]
