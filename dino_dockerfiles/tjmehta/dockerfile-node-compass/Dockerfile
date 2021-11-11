# Pull base image.
FROM dockerfile/nodejs

# Install Ruby.
RUN \
  apt-get update && \
  apt-get install -y ruby ruby-dev ruby-bundler && \
  rm -rf /var/lib/apt/lists/*

# Install Compass.
RUN gem install compass

# Set encoding for SASS
RUN locale-gen en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["bash"]
