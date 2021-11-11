FROM python:3.8

RUN apt-get update && apt-get install -y \
                              wget \
                              curl \
                              unzip \
                              zip \
                              git && \
    cd /tmp && wget https://releases.hashicorp.com/packer/1.2.2/packer_1.2.2_linux_amd64.zip -O packer.zip && \
    unzip packer.zip && \
    mv packer /usr/local/bin/packer && \
    rm packer*

RUN pip install \
        ansible==2.9.9 \
        awscli==1.18.35 \
        boto3==1.14.52

COPY bin/* /usr/bin/
