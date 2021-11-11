FROM node:lts-alpine
  
RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN npm install pm2 -g

USER node
RUN mkdir -p /home/node/app
WORKDIR /home/node/app

COPY . /home/node/app/


# Install app dependencies
ENV NPM_CONFIG_LOGLEVEL warn
RUN npm install --development

# Expose the listening port of your app
EXPOSE 8080

# Show current folder structure in logs
RUN ls -al -R

CMD [ "pm2-runtime", "start", "ecosystem.config.js" ]
