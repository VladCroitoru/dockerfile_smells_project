# Extend from some predefined docker on dockerhub. Currently using ubuntu disro
# Install nvidia-container
# Check the Gpu driver, cuda driver and cudnn version of 
# host system, use tag according to host sytem otherwise
# this will through error.
# At current time 
#   Host system is ubuntu:20.04
#   nvidia-driver on host system is 455
#   cuda version is 11.2


#FROM nvidia/cuda:11.2.2-cudnn8-devel-ubuntu20.04
FROM ubuntu
# Add labels to docker such as maintainer, version etc.
LABEL maintainer="vk001716@gmail.com"
LABEL version="0.1"


# ENV instruction adds env variable
ENV TEST="hello"

RUN echo $TEST

# MUST RUN THIS TWO LINE 
# set timezone according to your region
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Run instruction runs a command
RUN apt update
RUN apt install python3 python3-pip build-essential cmake make -y

# Install dlib package

# Install flask package

# RUN pip3 install dlib flask
RUN pip3 install  flask
# Lets copy contents of current folder to /docker-app folder in image

ADD ./ /docker-app

# What is the difference between CMD and ENTRYPOINT? You cannot override the ENTRYPOINT instruction by adding command-line parameters to the docker run command. By opting for this instruction, you imply that the container is specifically built for such use.

# Lets expose the image port to connect to flask applicaiton

EXPOSE 5000

# Entry point for docker image file
ENTRYPOINT  /usr/bin/python3 /docker-app/app/app.py
