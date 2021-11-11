FROM codeship/aws-deployment

RUN \
  curl -o /usr/local/bin/ecs-cli \
    https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest && \
  chmod 755 /usr/local/bin/ecs-cli