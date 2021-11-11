FROM node:6
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY package.json /usr/src/app/
RUN npm install
copy . /usr/src/app
CMD [ "node", "/usr/src/app/index.js" ]
