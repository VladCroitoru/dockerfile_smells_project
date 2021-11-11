FROM docker:latest
MAINTAINER Jesse DeFer <docker-compose@dotd.com>

RUN apk add --no-cache --update git openssh-client py-pip
RUN addgroup -g 1000 jenkins && addgroup -g 513 docker && adduser -D -u 1000 -g 1000 -G docker jenkins

RUN mkdir -p /home/jenkins/.ssh && chmod 0700 /home/jenkins/.ssh && echo "github.com ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ==" > /home/jenkins/.ssh/authorized_keys > /home/jenkins/.ssh/known_hosts && chmod 0600 /home/jenkins/.ssh/* && chown -R jenkins:jenkins /home/jenkins/.ssh

RUN pip install docker-compose
