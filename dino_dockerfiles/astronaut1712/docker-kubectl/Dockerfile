FROM google/cloud-sdk:slim

ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y libtool openssl curl tar gzip bash ca-certificates git gawk

RUN curl -L -o /usr/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl

RUN chmod +x /usr/bin/kubectl

CMD [ "kubectl" ]
