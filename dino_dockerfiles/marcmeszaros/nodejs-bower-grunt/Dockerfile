#
# Node.js w/ Bower & Grunt Dockerfile
#
# https://github.com/dockerfile/nodejs-bower-grunt
#

# Pull base image.
FROM dockerfile/nodejs

# Install Bower & Grunt
RUN npm install -g bower grunt-cli

# Define working directory.
WORKDIR /data

# Define volume mount point.
VOLUME ["/data"]

# Define default command.
CMD ["bash"]
