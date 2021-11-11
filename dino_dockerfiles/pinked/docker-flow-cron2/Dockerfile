FROM node:alpine
ENV DF_UPDATE_SCHEDULE */5 * * * * *
RUN mkdir /app
WORKDIR /app
COPY package.json .
RUN npm install -s --no-optional--prod
COPY . .

CMD npm start

HEALTHCHECK CMD wget -q localhost:3301 -O /dev/null || exit 1