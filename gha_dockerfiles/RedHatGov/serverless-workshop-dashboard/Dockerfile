FROM quay.io/redhatgov/workshop-dashboard:latest

USER root

# install aws2
RUN wget https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip && \
    unzip ./awscli-exe-linux-x86_64-2.0.30.zip && \
    rm ./awscli-exe-linux-x86_64-2.0.30.zip && \
    ./aws/install && \
    rm -rf ./aws

# install stern
RUN wget https://github.com/wercker/stern/releases/download/1.11.0/stern_linux_amd64 -O /usr/local/bin/stern && \
    chown 1001 /usr/local/bin/stern && \
    chmod 550 /usr/local/bin/stern

# install kn
RUN wget https://mirror.openshift.com/pub/openshift-v4/clients/serverless/0.17.3/kn-linux-amd64-0.17.3.tar.gz && \
    tar -xf ./kn-linux-amd64-0.17.3.tar.gz -C /usr/local/bin && \
    rm kn-linux-amd64-0.17.3.tar.gz && \
    chown 1001 /usr/local/bin/kn && \
    chmod 550 /usr/local/bin/kn

COPY . /tmp/src

RUN rm -rf /tmp/src/.git* && \
    chown -R 1001 /tmp/src && \
    chgrp -R 0 /tmp/src && \
    chmod -R g+w /tmp/src

ENV TERMINAL_TAB=split

USER 1001

RUN /usr/libexec/s2i/assemble
