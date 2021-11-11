FROM    node:8.12.0

# setup to install basic development environment
RUN     apt-get update && apt-get upgrade -y
RUN     apt-get install -y locales locales-all less man vim jq zip rsync

# set to swedish :)
ENV     LC_ALL=sv_SE.UTF-8
ENV     LANG=sv_SE.UTF-8
ENV     LANGUAGE=sv_SE.UTF-8

# setup to install AWS CLI
RUN     apt-get install -y python python-pip python-virtualenv python-dev
RUN     pip install awscli
# create symbolic links; requires use of secrets
RUN     mkdir ~/.aws && \
        ln -s /run/secrets/aws.config ~/.aws/config && \
        ln -s /run/secrets/aws.credentials ~/.aws/credentials

# install httpie after AWS since it also uses python/pip
RUN     pip install httpie

# setup angular development; allow for optional local npm registry
#ARG     REGISTRY=registry.npmjs.org
#RUN     npm set registry http://${REGISTRY}/
#RUN     npm install -g @angular/cli

WORKDIR /devel
CMD     exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
