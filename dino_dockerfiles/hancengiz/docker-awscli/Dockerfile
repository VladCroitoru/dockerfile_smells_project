FROM alpine:3.4
MAINTAINER Cengiz Han <cengiz@cengizhan.com>

RUN apk --update add \
      bash \
      curl \
      python \
      groff \
      less


RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
RUN unzip awscli-bundle.zip
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws


RUN curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest
RUN chmod +x /usr/local/bin/ecs-cli

RUN echo ==== AWS and ECS CLIs are installed ====
RUN aws --version
RUN ecs-cli --version
