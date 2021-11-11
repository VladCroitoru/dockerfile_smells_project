FROM node:latest

USER root

RUN mkdir -p /app/
WORKDIR /app/

COPY ./app/package.json /app/
RUN npm install

COPY ./app/ /app

RUN apt-get update && apt-get install -y \
mysql-client \
&& rm -rf /var/lib/apt/lists/*

EXPOSE 8080
CMD ["npm", "start"]
