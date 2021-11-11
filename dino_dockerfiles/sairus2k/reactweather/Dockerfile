FROM node:6.10.0

# Copy application files
COPY . /usr/src/app
WORKDIR /usr/src/app

# Install Yarn and Node.js dependencies
RUN npm install

CMD [ "node", "server.js" ]
