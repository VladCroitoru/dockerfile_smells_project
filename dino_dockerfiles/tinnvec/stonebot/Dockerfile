FROM ubuntu:16.04

# Add dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_7.x | bash && \
    apt-get update && \
    apt-get install -y automake build-essential git libtool nodejs python && \
    apt-get autoremove -y

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json \
    gulpfile.js \
    tsconfig.json \
    ./
RUN npm install

# Copy app source
COPY src ./src

CMD npm start
