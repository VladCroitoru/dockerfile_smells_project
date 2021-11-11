# Use an official Python runtime as a base image
FROM ubuntu:latest

# Install
RUN apt-get update
RUN apt-get install -y wget zip unzip awscli python python3 openjdk-8-jdk maven groff jq ansible git curl sshuttle
RUN wget https://releases.hashicorp.com/packer/1.0.3/packer_1.0.3_linux_amd64.zip
RUN unzip packer_1.0.3_linux_amd64.zip

