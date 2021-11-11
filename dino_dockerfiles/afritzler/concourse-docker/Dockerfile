FROM alpine:latest

ENV PATH $PATH:/usr/local/bin
ENV TERRAFORM_VER 0.7.3
ENV TERRAFORM_ZIP terraform_${TERRAFORM_VER}_linux_386.zip

ENV PACKER_VERSION 0.12.0 
ENV PACKER_ZIP packer_${PACKER_VERSION}_linux_amd64.zip

RUN apk add --update openssl openssh-client ca-certificates && rm -rf /var/cache/apk/*
RUN set -ex \
       && wget https://releases.hashicorp.com/terraform/${TERRAFORM_VER}/${TERRAFORM_ZIP} -O /tmp/${TERRAFORM_ZIP} \
       && unzip /tmp/${TERRAFORM_ZIP} -d /usr/local/bin  \
       && rm /tmp/${TERRAFORM_ZIP}

RUN set -ex \
       && wget https://releases.hashicorp.com/packer/${PACKER_VERSION}/${PACKER_ZIP} -O /tmp/${PACKER_ZIP} \
       && unzip /tmp/${PACKER_ZIP} -d /usr/local/bin  \
       && rm /tmp/${PACKER_ZIP}      

RUN apk add --update \                                                                                                                                                                                                                          
       python-dev \                                                                                                                                                                                                                             
       py-pip \                                                                                                                                                                                                                                 
       py-setuptools \                                                                                                                                                                                                                          
       gcc \                                                                                                                                                                                                                                    
       musl-dev \                                                                                                                                                                                                                               
       linux-headers \                                                                                                                                                                                                                          
       && pip install --upgrade --no-cache-dir python-openstackclient \                                                                                                                                                                         
       && apk del gcc musl-dev linux-headers                                                                                                                                                                                                    
                                                      
RUN apk add --update expect bash git curl && rm -rf /var/cache/apk/*
