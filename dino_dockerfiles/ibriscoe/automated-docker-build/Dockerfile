###########################################
# Dockerfile to build a new image
###########################################

# Base image is Ubuntu
FROM ubuntu:14.04

# Author: Dr. Peter
MAINTAINER I Briscoe <ijbriscoe@googlemail.com>

# create 'mynewdir' and 'mynewfile'
RUN mkdir mynewdir
RUN touch /mynewdir/mynewfile

# Write the message in file
RUN echo 'This is my new container to make image and then push to hub; also set up to do an automated build when pushed to GitHub' \
 >/mynewdir/mynewfile
