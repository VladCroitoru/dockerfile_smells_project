FROM codeship/aws-deployment

ENV ECS_ENVFILE /app.env
ENV ECS_DEPLOYMENT /deployment.yml

RUN \
  curl -o /usr/local/bin/ecs-cli \
    https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest && \
  chmod 755 /usr/local/bin/ecs-cli

RUN \
  curl -o /usr/local/bin/ecs-deploy \
    https://raw.githubusercontent.com/silinternational/ecs-deploy/master/ecs-deploy && \
  chmod 755 /usr/local/bin/ecs-deploy

ADD scripts /scripts
RUN chmod -R 755 /scripts
ENV PATH $PATH:/scripts
