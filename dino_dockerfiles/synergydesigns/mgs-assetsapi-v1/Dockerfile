FROM node:latest

MAINTAINER Synergy Designs <<synergydesigns@gmail.com>>

COPY . /var/www
# ADD . /var/wwww
WORKDIR /var/www

RUN ["npm", "install"]
RUN ["npm", "run", "build"]

CMD ["node", "dist/server.js"]