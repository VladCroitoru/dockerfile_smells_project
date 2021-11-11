FROM alpine
MAINTAINER tess@deninet.com

# Install packages.
RUN apk --update --no-cache add \
        python \
        py-pip \
        openssl \
        openssh-client \
        git \
        rsync \
        libressl2.5-libcrypto

# Install packages only needed for building.
RUN apk add --no-cache --virtual .build-dependencies \
        build-base \
        curl-dev \
        openssl-dev \
        python-dev \
        libffi-dev

RUN pip install \
         ansible \
         pycurl \
         linode-python

# Remove unneed packages
RUN apk del .build-dependencies
RUN rm -f /var/cache/apk/*

# Copy needed Ansible files
COPY hosts /etc/ansible/
COPY ansible.cfg /etc/ansible/

CMD ["ansible"]
