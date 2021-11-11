FROM amazonlinux:2

LABEL maintainer=OMBU

WORKDIR /tmp

RUN \
    yum install -y awscli python2-pip &&\
    curl -so session-manager-plugin.rpm \
    https://s3.amazonaws.com/session-manager-downloads/plugin/latest/linux_64bit/session-manager-plugin.rpm &&\
    yum install -y session-manager-plugin.rpm &&\
    rm session-manager-plugin.rpm &&\
    curl -so /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest &&\
    chmod u+x /usr/local/bin/ecs-cli &&\
    pip --no-cache-dir install awslogs cfn-lint &&\
    rm -rf /var/cache/yum/*
