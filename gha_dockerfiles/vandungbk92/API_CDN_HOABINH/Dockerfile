FROM node:12-alpine
RUN apk update && apk upgrade && apk add --no-cache git

WORKDIR /usr/src/app
COPY . .
RUN npm install && npm cache clean --force
RUN npm run build
EXPOSE 3001
CMD ["node", "dist/app.js"]
