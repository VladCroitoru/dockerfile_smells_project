FROM node

RUN mkdir -p /opt/build /usr/src/

COPY ./ /opt/build/
WORKDIR /opt/build

RUN npm install -g grunt-cli && npm install -g bower && npm install
RUN bower --allow-root install && grunt

RUN mv dist /usr/src/app
WORKDIR /usr/src/app

EXPOSE 3000
CMD [ "npm", "start" ]