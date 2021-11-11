FROM smebberson/alpine-nginx-nodejs:4.2.2

# Install global node dependencies
RUN npm install gulp -g

# Make an area to work in
RUN mkdir /workspace
WORKDIR /workspace

# Move over needed files
ADD package.json .
ADD src/ src/
ADD Gulpfile.js .

# Install local node dependencies
RUN npm install

# Build!
RUN gulp

# Move built files into proper nginx directory
RUN rm -rf /usr/html
RUN cp -R build /usr/html

# Remove workspace to decrease image size
RUN rm -rf /workspace
