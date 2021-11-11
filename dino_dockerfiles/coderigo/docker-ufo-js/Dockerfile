# Base image
FROM ubuntu:14.04

# Put my hand up as maintainer
MAINTAINER Rodrigo Martell <rodrigo.martell@gmail.com>

# Suppress debian frontend warnings from Ubuntu base image
RUN DEBIAN_FRONTEND=noninteractive

# Install OS tools we'll need
RUN \
    apt-get update && \
    apt-get -y install nodejs && \
    apt-get -y install npm && \
    apt-get -y install curl && \
    apt-get -y install vim && \
    apt-get -y install git && \
    apt-get -y install zsh

# Install OH-MY-ZSH to see pretty terminal and ditch the bash
RUN curl -L https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh | bash

# Make symbolic link to "node" since code was written for OSX and linux refers to "node" as "nodejs"
RUN ln -s /usr/bin/nodejs /usr/bin/node

# Clone the ufo-js repository, install dependencies and make binaries
RUN \
    git clone https://github.com/coderigo/ufo.js-base.git /root/ufo.js-base && \
    cd /root/ufo.js-base && \
    npm install && \
    make compile

# Expose port 9000 (used by ufo-js)
EXPOSE 9000

# Set environment variables
ENV HOME /root

# Define working directory
WORKDIR /root

# Define default command
CMD ["/bin/zsh"]