FROM hashicorp/consul-template:alpine
WORKDIR /consul-template

USER root

RUN apk --no-cache add curl

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl

COPY --chown=consul-template:consul-template src /consul-template

USER 100:1000
