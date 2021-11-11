FROM node:8.11.3-alpine

RUN mkdir -p /usr/src/app/app
WORKDIR /usr/src/app

COPY ["package.json", "package-lock.json", "/usr/src/app/"]
COPY app /usr/src/app/app
RUN export NODE_ENV=production
RUN npm install --only=production

EXPOSE 3000

HEALTHCHECK CMD curl --fail http://localhost:3000/status || exit 1

CMD npm start