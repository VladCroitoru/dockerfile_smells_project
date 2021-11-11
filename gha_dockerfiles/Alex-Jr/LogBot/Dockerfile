FROM node:16.10.0-alpine3.14

# Create app directory
WORKDIR /usr/src/app

# Copy app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

# Nameserver defined to ensure it works
# Install app and node dependencies
RUN echo "nameserver 1.1.1.1" > /etc/resolv.conf && \ 
  apk upgrade --update && \ 
  apk add --no-cache -t build-dependencies make gcc g++ python2 libtool autoconf automake youtube-dl && \
  npm install

# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . /usr/src/app/

RUN npm run build

CMD [ "npm", "start" ]
EXPOSE 9000