FROM node

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
COPY bower.json /usr/src/app/
COPY .jshintrc /usr/src/app/
COPY .bowerrc /usr/src/app/

RUN npm install  && npm install bower -g && npm install gulp -g && bower install --allow-root && npm install gulp-cli -g

# Bundle app source
COPY . /usr/src/app

EXPOSE 9000
CMD [ "gulp", "serve" ]
