# Run as:
# docker run -d --name infolis-webapp -p '3000:3000' infolis/infolis-web
FROM node:6.2

ENV NODE_ENV production
WORKDIR /app

RUN apt-get update -y && apt-get install -y raptor2-utils vim

COPY . /app
RUN npm --loglevel warn install
RUN npm run client

EXPOSE 3000
CMD npm run start
