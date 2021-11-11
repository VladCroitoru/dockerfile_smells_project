from docker:latest

RUN apk add --no-cache curl jq python py-pip libxml2-utils bash
RUN pip install awscli
COPY ecs-deploy /bin/ecs-deploy
RUN chmod +x /bin/ecs-deploy
