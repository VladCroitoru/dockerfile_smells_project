# Use the base CentOS image.  If systemd is required in the future, change to 'creativeux/centos-base-systemd'
FROM centos:7

MAINTAINER Adrian Jagnanan
USER root

# Install the EPEL repository
RUN yum -y install \
  epel-release

# Install core RPMs
RUN yum -y install \
  tar \
  bzip2

# Install required developer tools
RUN yum -y install \
  make \
  gcc \
  git \
  sudo

# Install node & npm and upgrade to desired versions.
RUN yum -y install \
  nodejs \
  npm && \
  npm install -g n && \
  n 6.10

# Install ruby
RUN yum -y install ruby \
  ruby-devel \
  rubygems

# Install compass
RUN gem install compass

# Install required libs
RUN yum -y install \
  libpng-devel

# Install Grunt and Bower
RUN npm install -g \
  grunt-cli \
  bower && \
  echo '{ "allow_root": true }' > /root/.bowerrc

# Install serverless
RUN npm install -g serverless@1.20.0

# Install aws-sdk
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
  python get-pip.py && \
  pip install awscli

# Print out versions
RUN node -v && \
  npm -v && \
  bower -v && \
  sls -v

# Clean up
RUN yum clean all && \
  npm cache clean -f

# Define working directory.
WORKDIR /data

# Define default command
CMD ["bash"]
