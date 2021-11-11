# Set the base image to Ubuntu
FROM ubuntu:14.04

# File Author / Maintainer
MAINTAINER Paulina Lach

#ENV http_proxy=http://wwwcache.rl.ac.uk:8080
#ENV https_proxy=http://wwwcache.rl.ac.uk:8080
#ENV HTTP_PROXY=http://wwwcache.rl.ac.uk:8080
#ENV HTTPS_PROXY=http://wwwcache.rl.ac.uk:8080


# Update the repository sources list
RUN apt-get update


# Add the package verification key
#RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10

# Add MongoDB to the repository sources list
#RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/mongodb.list

# Update the repository sources list once more
#RUN apt-get update

# Install MongoDB package (.deb)
RUN apt-get -y install gcc
#RUN apt-get update
# Create the default data directory
#RUN mkdir -p /data/db

##################### INSTALLATION END #####################

# Expose the default port
#EXPOSE 27017

ADD ./hello.c /home/hello.c
RUN gcc /home/hello.c -o /home/hello.out

# Default port to execute the entrypoint (MongoDB)
#CMD ["--port 27017"]

# Set default container command
ENTRYPOINT /home/hello.out
