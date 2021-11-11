FROM node:6-alpine

LABEL maintainer="Simon Emms <simon@simonemms.com>"

# Set the work directory and add the project files to it
WORKDIR /opt/app
ADD . /opt/app

ENV VH_HOSTS=""

RUN chown -Rf node /opt/app

USER node

RUN npm install --production

EXPOSE 3000

CMD [ "npm", "start" ]
