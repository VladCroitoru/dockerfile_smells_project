FROM node:6
MAINTAINER KeepItCool <keepitcool@gmail.com>

RUN mkdir -p /app
WORKDIR /app

ENV PORT 3000
ENV ROOT_DIR /files

COPY package.json /app/
RUN npm install

COPY app.js /app/
COPY swagger /app/swagger

CMD ["node", "app.js"]
