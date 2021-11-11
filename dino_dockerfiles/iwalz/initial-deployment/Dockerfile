FROM alpine

RUN apk add --update bash curl git openssh
RUN /usr/bin/curl -L -o /usr/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v1.4.3/bin/linux/amd64/kubectl && chmod +x /usr/bin/kubectl
RUN mkdir -p /root/.ssh/ && echo -e "Host *\n\tStrictHostKeyChecking no" > /root/.ssh/config
ADD run.sh /usr/local/bin/deployment.sh


ENTRYPOINT [ "/bin/bash", "/usr/local/bin/deployment.sh" ]