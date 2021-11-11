# Pull base image
FROM loansolutions/nginx-node:latest

MAINTAINER Raymond Torino <raymond@loansolutions.ph>

# Install and build the application
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install --unsafe-perm=true

COPY . /usr/src/app
RUN npm run build

COPY default.conf /etc/nginx/conf.d/

CMD ["nginx", "-g", "daemon off;"]
