FROM node:7

RUN apt-get update

RUN mkdir /app
WORKDIR /app

#install dependencies
RUN npm install -g grunt-cli

# refer to: https://github.com/Financial-Times/polyfill-service

#TODO: maybe make a switch for different polyfill versions
RUN wget https://github.com/Financial-Times/polyfill-service/archive/v3.18.1.tar.gz -P /tmp
RUN tar -xzf /tmp/v3.18.1.tar.gz -C /app/ --strip-components=1
RUN ls /app
RUN rm -f /tmp/v3.18.1.tar.gz
RUN npm install
RUN npm run build

ENV NODE_ENV prod

EXPOSE 3000
CMD ["npm", "start"]
