FROM golang:alpine as go-source
FROM hashicorp/terraform:latest as tf-source
FROM hashicorp/packer:latest as pack-source

FROM frolvlad/alpine-miniconda3:python3.7

ENV LANG C.UTF-8
ENV GOPATH /go
ENV GOROOT /usr/local/go
ENV PATH $GOPATH/bin:$GOROOT/bin:$PATH

RUN set -eux
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"

#RUN echo '@edge http://nl.alpinelinux.org/alpine/edge/main' >> /etc/apk/repositories
#RUN echo '@edgecommunity http://nl.alpinelinux.org/alpine/edge/community' >> /etc/apk/repositories
#RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories

RUN apk add --no-cache ca-certificates alpine-sdk docker \
    zip nmap nano tar openssl openssl-dev \
    bash bash-completion curl wget jq \
    libffi-dev libc-dev linux-headers openssh \
    bind-tools coreutils groff

RUN wget -O /usr/local/bin/aws-sudo https://raw.githubusercontent.com/cleardataeng/aws-sudo/master/aws-sudo.sh
RUN chmod +x /usr/local/bin/aws-sudo

COPY --from=tf-source /bin/terraform /usr/local/bin/terraform
COPY --from=pack-source /bin/packer /usr/local/bin/packer
RUN mkdir -p /usr/local/go
COPY --from=go-source /usr/local/go /usr/local/go
COPY files/.profile /tmp/
COPY files/.bashrc /tmp/
COPY files/.gitconfig /root/

RUN touch ~/.profile \
    && touch ~/.bashrc \
    && cat /tmp/.profile >> ~/.profile \
    && cat /tmp/.bashrc >> ~/.bashrc \
    && rm -rf /tmp/.profile /tmp/.bashrc \
    && chmod 750 ~/.profile \
    && chmod 750 ~/.bashrc \
    && chmod 644 ~/.gitconfig \
    && sed -i 's/\/root:\/bin\/ash/\/root:\/bin\/bash/g' /etc/passwd

RUN wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash

SHELL ["/bin/bash", "-c"]

RUN conda init bash
RUN conda update -y -n base -c defaults conda
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf ./aws awscliv2.zip && \
    echo "complete -C aws_completer aws" >> ~/.bashrc

WORKDIR /root/

CMD ["bash", "-il"]
