FROM hashicorp/terraform:0.11.0-beta1

WORKDIR /usr/local/deployer

ADD . /usr/local/deployer

ENTRYPOINT src/loop.sh
