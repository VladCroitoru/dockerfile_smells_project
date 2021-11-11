FROM python:3.6.4

# Install node prereqs, nodejs and yarn
# Ref: https://deb.nodesource.com/setup_8.x
# Ref: https://yarnpkg.com/en/docs/install

COPY . /usr
WORKDIR /usr

RUN apt-get update
RUN apt-get install -yqq apt-transport-https jq
RUN pip install awscli docker-compose
RUN curl -o /usr/local/bin/ecs https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest
RUN chmod +x /usr/local/bin/ecs

RUN export PYTHONUSERBASE=packages && pip install -r requirement.txt --user
