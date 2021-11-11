FROM delitescere/jdk:8

MAINTAINER Rajat Vig <rajat.vig@gmail.com>

ARG VCS_REF
ARG IMAGE_VERSION

LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/rajatvig/docker-local-dynamo-alpine" \
      org.label-schema.name="local-dynamo-alpine" \
      org.label-schema.description="Run DynamoDB locally using the Amazon provided JAR with JDK" \
      org.label-schema.version=$IMAGE_VERSION \
      org.label-schema.schema-version="1.0" \
      org.label-schema.docker.cmd="docker run -d -t -p 8000:8000 rajatvig/local-dynamo-alpine:latest"

ENV DATADIR /var/lib/dynamo

USER root

RUN addgroup -g 9999 docker && \
  adduser -u 9999 -G docker -D -g "Docker User" docker

RUN mkdir $DATADIR && chown docker:docker $DATADIR
USER docker

WORKDIR /home/docker

RUN wget -O /home/docker/dynamodb_local_latest.tar.gz http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest && \
  tar xzf /home/docker/dynamodb_local_latest.tar.gz && \
  rm /home/docker/dynamodb_local_latest.tar.gz

EXPOSE 8000
VOLUME $DATADIR

COPY cmd.sh /home/docker/cmd.sh

CMD ["/home/docker/cmd.sh", "-dbPath /var/lib/dynamo"]
