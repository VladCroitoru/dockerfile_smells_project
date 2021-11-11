FROM node:argon
MAINTAINER Tom Schaible <tschaible@gmail.com>

#setup environment
ENV PORT=3000
ENV NODE_ENV=production

# create directory for app
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json app.js /usr/src/app/
COPY routes /usr/src/app/routes
COPY modules /usr/src/app/modules
COPY bin /usr/src/app/bin

RUN npm install -g forever
RUN npm install



EXPOSE ${PORT}


CMD ["forever","-a","--uid","slack-weather","/usr/src/app/bin/www"]
