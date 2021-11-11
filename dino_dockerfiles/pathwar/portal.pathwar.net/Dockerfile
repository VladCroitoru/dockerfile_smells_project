FROM node:0.10

# NPM
COPY package.json /usr/src/
RUN cd /usr/src && npm install

# APP
COPY . /usr/src/app/
ENV PATH /usr/src/node_modules/.bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
WORKDIR /usr/src/app/
RUN npm run prestart
EXPOSE 8090 35729
CMD npm start
