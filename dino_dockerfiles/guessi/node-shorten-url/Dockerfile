FROM node:12-alpine
ADD index.js package.json yarn.lock /opt/app/
WORKDIR /opt/app
RUN yarn install
VOLUME /opt/app/config/
EXPOSE 8080
CMD [ "node", "/opt/app/index.js" ]
