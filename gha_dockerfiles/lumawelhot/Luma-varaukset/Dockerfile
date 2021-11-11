FROM node:16-alpine AS build

WORKDIR /usr/src/app

COPY ./frontend .

ARG PUBLIC_URL
ENV PUBLIC_URL=$PUBLIC_URL

RUN npm ci --production && \
    npm run build --prod

FROM node:16-alpine

WORKDIR /app/backend

COPY --from=build /usr/src/app/build /app/backend/build

COPY ./backend .

RUN npm ci --production

EXPOSE 3001

USER node

CMD ["npm", "start"]