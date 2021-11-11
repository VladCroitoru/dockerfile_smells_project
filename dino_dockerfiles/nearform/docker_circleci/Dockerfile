FROM circleci/golang:1.9-stretch
LABEL maintainer alex.knol@nearform.com

ENV S2I_VERSION v1.1.9a
ENV SKOPEO_VERSION 0.1.28

RUN \
    cd ~ && \
    S2I_VERSION_COMPLETE="$S2I_VERSION-40ad911d" && \
    URL="https://github.com/openshift/source-to-image/releases/download/$S2I_VERSION/source-to-image-$S2I_VERSION_COMPLETE-linux-amd64.tar.gz" && \
    wget "$URL" && \
    tar zxvf "source-to-image-$S2I_VERSION_COMPLETE-linux-amd64.tar.gz" && \
    sudo mv ./s2i /usr/local/bin && \
    sudo apt-get update -qq && \
    sudo apt-get install -qqy \
        python-dev \
        python-setuptools \
        build-essential \
        jq \
        git-core \
        libdevmapper-dev \
        libgpgme11-dev \
        btrfs-tools \
        go-md2man \
        libglib2.0-dev \
        libostree-dev && \
    sudo rm -rf /var/lib/apt/lists/* && \
    go env GOPATH && \
    go get -u github.com/magefile/mage && \
    cd $GOPATH/src/github.com/magefile/mage && \
    go run -v bootstrap.go && \
    go get -u github.com/spf13/viper && \
    go get -u github.com/docker/docker/client && \
    go get -u github.com/mholt/archiver && \
    sudo easy_install pip && \
    sudo pip install https://github.com/goldmann/docker-squash/archive/master.zip && \
    sudo pip install python-dateutil && \
    sudo pip install --no-deps s3cmd && \
    curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" && \
    unzip awscli-bundle.zip && \
    sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \
    git clone https://github.com/projectatomic/skopeo $GOPATH/src/github.com/projectatomic/skopeo && \
    cd $GOPATH/src/github.com/projectatomic/skopeo && make binary-local && \
    sudo mv skopeo /usr/bin/
