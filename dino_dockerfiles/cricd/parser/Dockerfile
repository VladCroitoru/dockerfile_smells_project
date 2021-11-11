
############################################################
# Dockerfile to run cricd-parser
############################################################

FROM node:alpine
MAINTAINER Bradley Scott

# Copy code to container
RUN mkdir parser
COPY . /parser

# Get dependencies
RUN cd parser \
	&& npm install

# Define working directory.
WORKDIR /parser

# Start the service
CMD npm start

# Expose ports.
EXPOSE 3000
