FROM node:lts-alpine

LABEL org.opencontainers.image.source https://github.com/chickaree/web

EXPOSE 80

ENV PORT 80

COPY . /app

WORKDIR /app

RUN npm install --unsafe-perm --verbose; \
  npm run build;

CMD npm start;
