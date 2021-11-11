FROM library/node:latest
MAINTAINER Jujhar Singh <jujhar+docker@jujhar.com>

# Install Bower & Grunt
RUN npm install -g bower gulp-cli && \
    echo '{ "allow_root": true }' > /root/.bowerrc

# Define working directory, where you should map your project to
WORKDIR /data

# Define default command.
CMD ["bash"]
