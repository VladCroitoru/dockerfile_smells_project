FROM mhart/alpine-node
MAINTAINER marklkelly@gmail.com

RUN apk update && apk add unzip curl python openntpd

RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" 
RUN unzip awscli-bundle.zip \
&& ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws 

RUN mkdir -p /home/projects

RUN npm install -g serverless@beta

