#
# NodeJS 8.11 Build Image
# Docker image with libraries and tools as required for building NodeJS 8.11 projects using Yarn 
#

FROM node:8.11.1-alpine
MAINTAINER Agile Digital <info@agiledigital.com.au>
LABEL Description="Docker image with libraries and tools as required for building NodeJS 8.11 projects using Yarn" Vendor="Agile Digital" Version="0.1"

ENV HOME /home/jenkins
RUN addgroup -S -g 10000 jenkins
RUN adduser -S -u 10000 -h $HOME -G jenkins jenkins

RUN  apk add --no-cache git

WORKDIR /home/jenkins
USER jenkins
