FROM registry.access.redhat.com/ubi7/ubi:latest

#FROM node:slim

USER root
RUN curl -sL https://rpm.nodesource.com/setup_14.x | bash -
RUN yum install -y  nodejs
RUN npm install -g serverless
