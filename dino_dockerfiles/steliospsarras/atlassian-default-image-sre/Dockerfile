FROM atlassian/default-image:2

MAINTAINER Stelios Psarras <stelios.psarras@cyantific.net>

RUN \
    # update repositories indexes
    apt-get update -y && \
    apt-get upgrade -y && \
    # install some basic tooling
    apt-get install -y jq unzip && \
    # install pip
    curl -O https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && \
    # install AWS CLI
    pip install awscli && \ 
    # install Ansible
    apt-get install -y ansible && \
    # install Google Cloud SDK (instructions taken from https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu)
    export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update -y && apt-get install google-cloud-sdk -y && \
    # install Packer
    cd /root && mkdir tmp && cd tmp && \
    curl https://releases.hashicorp.com/packer/1.2.3/packer_1.2.3_linux_amd64.zip > packer.zip && \
    unzip packer.zip && \
    mv packer /usr/bin/ && \
    rm -f packer.zip && \
    # install Terraform
    cd /root/tmp && \
    curl https://releases.hashicorp.com/terraform/0.11.7/terraform_0.11.7_linux_amd64.zip > terraform.zip && \
    unzip terraform.zip && \
    mv terraform /usr/bin/ && \
    rm -f terraform.zip && \
    # clean apt-get caches
    rm -rf /var/lib/apt/lists/*    
