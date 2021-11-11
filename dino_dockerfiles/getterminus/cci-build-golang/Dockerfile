FROM golang:1.15.7

RUN apt-get update && apt-get install -y \
    zip apt-transport-https ca-certificates \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common \
    python

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -

RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"

RUN apt-get update && apt-get install -y docker-ce

# Getting pip
RUN curl -O https://bootstrap.pypa.io/get-pip.py
# Installing pip
RUN python get-pip.py --user

ENV PATH $PATH:/root/.local/bin

# Installing aws-cli
RUN pip install awscli --upgrade --user
# Getting the version from aws-cli
RUN aws --version


RUN go get github.com/golang/dep/cmd/dep
RUN go get github.com/onsi/ginkgo/ginkgo
RUN mkdir $HOME/.docker && \
    echo "{\n  \"credsStore\": \"ecr-login\"\n}" > $HOME/.docker/config.json
RUN go get github.com/awslabs/amazon-ecr-credential-helper/ecr-login/cli/docker-credential-ecr-login
RUN go get github.com/GetTerminus/convox-off-cluster-builder/cmd/convox-build-off-cluster


ADD https://convox.com/cli/linux/convox /usr/local/bin/convox
RUN chmod 755 /usr/local/bin/convox
