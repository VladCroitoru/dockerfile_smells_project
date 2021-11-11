#
# broken-link-checker Dockerfile
#
# https://github.com/
#

# Pull base image.
FROM debian:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >

# Update & install packages
RUN apt-get update && \
    apt-get install -y gnupg git curl apt-transport-https

#Add yarn repository
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - 

# Update & install packages
RUN apt-get update && \
    apt-get install -y nodejs

# Install
RUN npm install broken-link-checker -g

# Let's GO!!
CMD blc $YOUR_URL -ro
