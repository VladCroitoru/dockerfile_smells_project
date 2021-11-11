FROM node:4.2.2

# Bundle app source
COPY . /src
# Remove node_modules that got copied over
RUN rm -rf /src/node_modules
# Remove bower components
RUN rm -rf /src/bower_components

# Install app dependencies
RUN cd /src; npm install

RUN npm install -g bower
RUN cd /src; bower install --allow-root

# Expose the applications default port
EXPOSE 3000

# Run the application
CMD ["node", "/src/server.js"]
