FROM alpine:latest

RUN wget -O /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/$(wget -qO- https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl \
    && chmod +x /usr/local/bin/kubectl

RUN apk add bind-tools

ADD patch.sh /patch.sh

RUN chmod 777 /patch.sh

CMD /patch.sh