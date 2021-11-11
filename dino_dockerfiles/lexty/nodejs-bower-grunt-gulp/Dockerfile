FROM node:4
MAINTAINER Alexander Medvedev <alexandr.mdr@gmail.com>

# Install Bower, Grunt and Gulp
RUN npm install -g bower grunt-cli && \
    echo '{ "allow_root": true }' > /root/.bowerrc
RUN npm install gulp -g

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["bash"]
