FROM circleci/golang:1.13.5-stretch-node-browsers-legacy
MAINTAINER ops@spaceback.me

# Install awscli
# http://docs.aws.amazon.com/cli/latest/userguide/awscli-install-bundle.html
RUN wget "s3.amazonaws.com/aws-cli/awscli-bundle.zip" -O "awscli-bundle.zip" && \
    unzip awscli-bundle.zip && \
    # Workaround to get awscli to work properly
    # https://github.com/aws/aws-cli/issues/1957#issuecomment-271057166
    sudo apt-get install groff-base && \
    sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \
    rm awscli-bundle.zip && \
    rm -rf awscli-bundle

#Install newman 
RUN sudo curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash - && \
    sudo sudo apt-get install -y nodejs && \
    sudo npm install newman -g

RUN set -x \
    VER="17.12.1-ce" \
    curl -L -o /tmp/docker-$VER.tgz https://download.docker.com/linux/static/stable/x86_64/docker-$VER.tgz \
    tar -xz -C /tmp -f /tmp/docker-$VER.tgz \
    mv /tmp/docker/* /usr/bin
WORKDIR /

ENTRYPOINT ["/bin/bash"]
