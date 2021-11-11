FROM maven:3-jdk-8
MAINTAINER myyk.seok@gmail.com

# Install AWS CLI
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
RUN unzip awscli-bundle.zip
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

# Install jQuery CLI
RUN apt-get update && apt-get install jq
