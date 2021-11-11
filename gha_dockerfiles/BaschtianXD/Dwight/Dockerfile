ARG NODE_ENV=production

FROM node:14-alpine
RUN apk add --no-cache ffmpeg
ENV NODE_ENV=${NODE_ENV}
WORKDIR /usr/src/app
COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
RUN npm install --silent
COPY . .
RUN npm run build
USER 405
CMD ["npm", "start"]

EXPOSE 8080
