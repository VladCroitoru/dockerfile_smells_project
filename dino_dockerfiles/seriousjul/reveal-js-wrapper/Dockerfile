FROM node:6-alpine

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install

FROM httpd:2-alpine

# Bundle app source
COPY --from=0 /usr/src/app /usr/local/apache2/htdocs/
COPY . /usr/local/apache2/htdocs/
RUN mv /usr/local/apache2/htdocs/httpd.conf /usr/local/apache2/conf/httpd.conf
