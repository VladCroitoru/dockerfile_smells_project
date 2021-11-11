FROM node:4.8.3-alpine

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install make
RUN apk update && \
    apk upgrade && \
    apk add make

# Install app dependencies
COPY package.json /usr/src/app
COPY Makefile /usr/src/app
RUN make install

# Bundle app source
COPY . /usr/src/app

EXPOSE 3000
CMD [ "make", "start" ]
