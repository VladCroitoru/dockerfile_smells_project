############################################################
# Dockerfile to build Node.js Sinopia
# Based on Node
############################################################

# Set the base image to CentOS
FROM centos:centos6

# File Author / Maintainer
MAINTAINER "Jash Lee" <s905060@gmail.com>

# Clean up yum repos to save spaces
RUN yum update -y >/dev/null

# Install epel
RUN yum -y install epel-release

# Install nodejs && npm
RUN yum -y install git nodejs npm --enablerepo=epel

# Sinopia Version / Path / Backup
ENV version v1.4.0
RUN git clone https://github.com/rlidwka/sinopia
WORKDIR /sinopia
RUN git checkout $version
RUN npm install --production

# Clean
RUN rm -rf .git
RUN npm cache clean

# Adding the run file
ADD config.yaml /sinopia/config.yaml

# Sinopia service port
EXPOSE 4873

# Mounted config
VOLUME ["/sinopia/storage"]

# Start the Sinopia service
CMD ["./bin/sinopia"]
