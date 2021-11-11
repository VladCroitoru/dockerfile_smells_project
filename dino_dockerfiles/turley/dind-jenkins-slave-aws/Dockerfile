# Docker-in-Docker Jenkins Slave, with awscli and ecs-deploy

FROM tehranian/dind-jenkins-slave
MAINTAINER Ben Turley <code@benturley.com>

# Upgrade packages
RUN apt-get -q update &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q upgrade -y -o Dpkg::Options::="--force-confnew" --no-install-recommends &&\
    apt-get -q autoremove &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

# Install AWS CLI and silinternational/ecs-deploy script
WORKDIR /root
RUN apt-get -q update && DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew" --no-install-recommends \
        unzip \
        python \
        jq &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin &&\
    wget -O awscli-bundle.zip https://s3.amazonaws.com/aws-cli/awscli-bundle.zip && unzip awscli-bundle.zip &&\
    ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && rm -rf ./awscli-bundle* &&\
    wget -O /usr/local/bin/ecs-deploy https://raw.githubusercontent.com/silinternational/ecs-deploy/master/ecs-deploy &&\
    chmod +x /usr/local/bin/ecs-deploy
